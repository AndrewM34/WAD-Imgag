from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from imgag.forms import UserForm, UserProfileForm
from imgag.models import UserProfile, Category, Upload, Comment
from imgag.webhose_search import run_query


#
def home(request):
	context = {}
	return render(request, 'imgag/home.html', context)


#
def about(request):
	context = {}
	return render(request, 'imgag/about.html', context)


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


# view to reset the password
# def reset_pass(request):
# 	context = {}
# 	if request.method == 'POST':
# 		context['username'] = request.POST.get('username')
#
# 	return render(request, 'imgag/reset_password.html', context)


# view to show account (details)
# should pass the username, profile picture and all posts by that user
@login_required
def account(request, user): # takes username as an arg
	context = {}
	context['username'] = user
	context['posts'] = Upload.objects.get(username=user)

	return render(request, 'imgag/account.html', context)


# view to change password
# https://github.com/macdhuibh/django-registration-templates/tree/master/registration
# @login_required
# def change_pass(request):
# 	pass


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
def post(request, hashid):
	post = Upload.objects.get(hashid=hashid)
	post_url = post.url_hash
	context = {}
	context['header'] = post.header
	context['category'] = post.category
	context['upVotes'] = post.up_votes
	context['downVotes'] = post.down_votes
	context['user'] = post.user
	context['media'] = post.media

	return render(request, 'imgag/'+post_url+'/', context)
	

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
