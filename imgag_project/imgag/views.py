from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from imgag.webhose_search import run_query
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json
from imgag.forms import UserForm, UserProfileForm, CommentForm
from imgag.models import UserProfile, Category, Upload, Comment, Vote

POSTS_ON_ONE_PAGE = 15


def get_num_page_and_offset(page):
	if page is not None:
		page = int(page) if int(page) > 0 else 1
	else:
		page = 1
	offset = (page - 1) * POSTS_ON_ONE_PAGE
	return page, offset

def home(request, page=1, ajax=None):
	page, offset = get_num_page_and_offset(page)
	posts = Upload.objects.filter(created_date__lte=timezone.now()) \
                .order_by('-created_date')[offset:offset + POSTS_ON_ONE_PAGE]
	posts_dict = [p.as_json() for p in posts]
	if ajax == "ajax":
		pass
	context_dict = {"posts": posts_dict, "page": page}
	return render(request, 'imgag/home.html', context_dict)


def about(request):
	return render(request, 'imgag/about.html')


def faq(request):
	return render(request, 'imgag/faq.html')


# view for registering a user
def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request, 'imgag/register.html',
				  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


# view for a user to login
def user_login(request):
	badlogin = False
	print("ejeej")
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				if "next" in request.GET:
					print("next here")
					return HttpResponseRedirect(request.GET["next"])
				print("next noooooooooooooot here")
				return HttpResponseRedirect(reverse('home'))

			else:
				return HttpResponse("Your Imgag account is disabled.")  # naughty user probably got banned

		else:
			badlogin = True
			return render(request, 'imgag/login.html', {"username": username, "badlogin": badlogin})

	else:
		return render(request, 'imgag/login.html', {'badlogin': badlogin})


# log out the current user
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


# view to show account (details)
# should pass the username, profile picture and all posts by that user
@login_required
def account(request): # takes username as an arg
	context = {}
	user = UserProfile.objects.get(user=request.user)
	#print (user)
	context['username'] = request.user
	#print (request.user)
	context['posts'] = Upload.objects.filter(author=user)

	return render(request, 'imgag/profile.html', context)


# view to show all categories
def show_categories(request):
	categories_list = [c.as_json() for c in Category.objects.all()]
	context_dict = {"categories": categories_list}
	return render(request, 'imgag/categories.html', context_dict)


def show_category(request, category_name_slug, page=None, ajax=None):
	page, offset = get_num_page_and_offset(page)
	category = Category.objects.get(slug=category_name_slug)
	if ajax == "ajax":
		pass
	posts_list = [p.as_json()
				  for p in
                  Upload.objects.filter(category=category).filter(created_date__lte=timezone.now())
                      .order_by("-created_date")[offset:offset + POSTS_ON_ONE_PAGE]]
	context_dict = {"category": category, "posts": posts_list, "page": page}

	return render(request, 'imgag/category.html', context_dict)


# view of a post
def show_post(request, post_hashid):
	print ("Gets into show post...")
	try:
		context_dict = {'comment_form': CommentForm()}
		post = Upload.objects.get(hashid=post_hashid)
		if post.created_date > timezone.now():
			raise ValueError
		context_dict['post'] = post.as_json()
		context_dict['up_votes'] = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__gte=1).count()
		context_dict['down_votes'] = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__lte=-1).count()
		context_dict['comments'] = [c.as_json() for c in Comment.objects.filter(upload=post)
			.filter(created_date__lte=timezone.now()).order_by("created_date")]
		if post.uploaded_file.name.endswith(".mp4"):
			context_dict['video'] = True
		else:
			context_dict['video'] = False
	except(ValueError, TypeError, Upload.DoesNotExist):
		pass
	return render(request, 'imgag/post.html', context_dict)

@login_required
def add_comment(request, post_hashid, comments_count=0, ajax=None):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = UserProfile.objects.get(user=request.user)
			try:
				comment.upload = Upload.objects.get(hashid=post_hashid)
				comment.save()
			except(TypeError, Upload.DoesNotExist):
				pass
		else:
			print(form.errors)
	if ajax == "ajax":
		new_comments = Comment.objects.filter(upload__hashid=post_hashid) \
                           .filter(created_date__lte=timezone.now()).order_by("created_date")[int(comments_count):]
		comments_json_dict = [c.as_json() for c in new_comments]
		json_dict = {"ok": True, "comments": comments_json_dict}
		return HttpResponse(json.dumps(json_dict), content_type="application/json")
	return HttpResponseRedirect(reverse('post', kwargs={'post_hashid': post_hashid}))

@login_required
def vote(request, post_hashid, users_vote, ajax=None):
	if request.method == 'POST':
		user = UserProfile.objects.get(user=request.user)
		post = Upload.objects.get(hashid=post_hashid)
		vote = Vote.objects.get_or_create(user=user, upload=post)[0]
		vote.vote = users_vote
		vote.save()
	if ajax == "ajax":
		up_votes = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__gte=1).count()
		down_votes = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__lte=-1).count()
		json_dict = {"ok": True, "up_votes": up_votes, "down_votes": down_votes}
		return HttpResponse(json.dumps(json_dict), content_type="application/json")
	return HttpResponseRedirect(reverse('post', kwargs={'post_hashid': post_hashid}))

# view for search
@csrf_exempt
def search(request):
	result_list = []
	query_human = ""
	if request.method == 'POST':
		query_human = request.POST['value']
		query = query_human.strip()
		if query:
			result_list = run_query(query)
	return render(request, 'imgag/search.html', {'result_list' : result_list, 'query_human':query_human})

@csrf_exempt
def searchArg(request, query):
	result_list = []
	human_readable = query.replace('_', ' ')
	value = human_readable.strip()
	if value:
		result_list = run_query(value)
	return render(request, 'imgag/search.html', {'result_list' : result_list, 'query_human':human_readable})

def test(request):
	return render(request, 'imgag/test.html', {})



@login_required
def upload(request):
	user = UserProfile.objects.get(user=request.user)
	cat = Category.objects.get(name="Deep")
	upload = Upload.objects.get_or_create(author=user, header=request.POST['header'], category=cat)[0]
	upload.uploaded_file=request.FILES['file']
	upload.save()
	print ("Upload created...")
	return home(request)

