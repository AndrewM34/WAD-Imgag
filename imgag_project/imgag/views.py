from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from imgag.forms import CategoryForm, PageForm, UserForm, UserProfileForm

#
def index(request):
    context = {}

    return render(request, 'imgag/index.html', context)


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

    return render(request, 'imgag/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


# view for a user to login
def login(request):
    badlogin = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Your Imgag account is disabled.") # naughty user probably got banned

        else:
            badlogin = True
            return render(request, 'imgag/login.html', {"username": username, "badlogin":badlogin})

else:
    return render(request, 'imgag/login.html', {'badlogin': badlogin})

# log out the current user
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# view to reset the password
def resetPass(request):
    pass


# view to show account (details)
@login_required
def account(request):
    pass


# view to change password
def changePass(request):
    pass


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
def post(request):
    postUrl = Upload.url_hash
    context = {}
    context['header'] = Upload.header
    context['category'] = Upload.category
    context['upVotes'] = Upload.upVotes
    context['downVotes'] = Upload.downVotes
    context['user'] = Upload.user
    context['media'] = Upload.media

    return render(request, 'imgag/'+postUrl+'/', context)
