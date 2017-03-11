from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from imgag.webhose_search import run_query
import json
from imgag.forms import UserForm, UserProfileForm, CommentForm
from imgag.models import UserProfile, Category, Upload, Comment, Vote


def home(request):
	return render(request, 'imgag/home.html', {})


def about(request):
	return render(request, 'imgag/about.html', {})


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
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
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
def categories(request, category_name_slug):
	context_dict = {}

	try:
		category = Category.objects.get(slug=category_name_slug)
		uploads = Upload.objects.filter(category=category)

		context_dict['uploads'] = uploads
		context_dict['category'] = category

	except Category.DoesNotExist:
		context_dict['uploads'] = None
		context_dict['category'] = None

	return render(request, 'imgag/category.html', context_dict)


# view of a post
def post(request, post_hashid):
	try:
		context_dict = {'comment_form': CommentForm()}
		post = Upload.objects.get(hashid=post_hashid)
		author = post.author.user.username
		context_dict['hashid'] = post_hashid
		context_dict['header'] = post.header
		context_dict['author'] = author
		context_dict['posted_date'] = post.created_date
		context_dict['upload'] = post.uploaded_file
		context_dict['up_votes'] = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__gte=1).count()
		context_dict['down_votes'] = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__lte=-1).count()
		context_dict['comments'] = Comment.objects.filter(upload=post).order_by("created_date")
		if post.uploaded_file.name.endswith(".mp4"):
			context_dict['video'] = True
		else:
			context_dict['video'] = False
	except(TypeError, Upload.DoesNotExist):
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
		new_comments = Comment.objects.filter(upload__hashid=post_hashid).order_by("created_date")[int(comments_count):]
		json_dict = [c.as_json() for c in new_comments]
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
		json_dict = {"up_votes": up_votes, "down_votes": down_votes}
		return HttpResponse(json.dumps(json_dict), content_type="application/json")
	return HttpResponseRedirect(reverse('post', kwargs={'post_hashid': post_hashid}))

# view for search
def search(request):
	result_list = []
	query_human = ""
	if request.method == 'POST':
		query_human = request.POST['query']
		query = query_human.strip()
		if query:
			result_list = run_query(query)
	return render(request, 'imgag/search.html', {'result_list' : result_list, 'query_human':query_human})


def test(request):
	return render(request, 'imgag/test.html', {})

def upload(request):
	user = UserProfile.objects.get(user=request.user)
	cat = Category.objects.get(name="Deep")
	upload = Upload.objects.get_or_create(author=user, header=request.POST['header'], category=cat)[0]
	upload.uploaded_file=request.FILES['file']
	upload.save()
	return post(request, upload.hashid.hashid)

