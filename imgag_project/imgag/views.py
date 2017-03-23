import sys, traceback
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from imgag.webhose_search import run_query
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import pytz
import json
from imgag.forms import CommentForm
from imgag.models import UserProfile, Category, Upload, Comment, Vote

POSTS_ON_ONE_PAGE = 15


def get_num_page_and_offset(page):
    if page is not None:
        page = int(page) if int(page) > 0 else 1
    else:
        page = 1
    offset = (page - 1) * POSTS_ON_ONE_PAGE
    return page, offset


def auth_and_older_than_18(request):
    try:
        return request.user.is_authenticated() and UserProfile.objects.get(user=request.user).older_than_18()
    except UserProfile.DoesNotExist:
        return False


def home(request, page=1, ajax=None):
    page, offset = get_num_page_and_offset(page)
    posts = Upload.objects.filter(created_date__lte=timezone.now()).order_by(
        '-created_date')[offset:offset + POSTS_ON_ONE_PAGE]
    posts_list = [p.as_json() for p in posts]
    context_dict = {"posts": posts_list, "page": page,
                    "user_can_see_nsfw": auth_and_older_than_18(request)}
    if ajax == "ajax":
        context_dict["ok"] = "ok"
        return HttpResponse(json.dumps(context_dict), content_type="application/json")
    return render(request, 'imgag/home.html', context_dict)


def about(request):
    return render(request, 'imgag/about.html')


def faq(request):
    return render(request, 'imgag/faq.html')


# view to show account (details)
# should pass the username, profile picture and all posts by that user
@login_required
def account(request):  # takes username as an arg
    try:
        user = UserProfile.objects.get(user=request.user)
        category_list = Category.objects.all()
        context = {'categories': category_list, 'username': request.user, 'userprofile': user}
        posts = Upload.objects.filter(author=user)
        posts_dict = [p.as_json() for p in posts]
        context['posts'] = posts_dict
        return render(request, 'imgag/profile.html', context)  # view to show all categories
    except UserProfile.DoesNotExist:
        return faq(request)


def show_categories(request):
    categories_list = [c.as_json() for c in Category.objects.all()]
    context_dict = {"categories": categories_list}
    return render(request, 'imgag/categories.html', context_dict)


def show_category(request, category_name_slug, page=None, ajax=None):
    page, offset = get_num_page_and_offset(page)
    category = Category.objects.get(slug=category_name_slug)
    posts_list = [p.as_json()
                  for p in
                  Upload.objects.filter(category=category).filter(created_date__lte=timezone.now()).order_by(
                      "-created_date")[offset:offset + POSTS_ON_ONE_PAGE]]
    context_dict = {"category": category.as_json(), "posts": posts_list, "page": page,
                    "user_can_see_nsfw": auth_and_older_than_18(request)}
    if ajax == "ajax":
        context_dict["ok"] = "ok"
        return HttpResponse(json.dumps(context_dict), content_type="application/json")
    return render(request, 'imgag/category.html', context_dict)


# view of a post
def show_post(request, post_hashid):
    context_dict = {}
    try:
        context_dict = {'comment_form': CommentForm()}
        post = Upload.objects.get(hashid=post_hashid)
        # We allow just hashed id to access a post, not its real id
        if str(post.hashid.hashid) != str(post_hashid):
            raise TypeError
        # Show only posts that weren't created in future
        if post.created_date > timezone.now():
            raise ValueError
        context_dict['post'] = post.as_json()
        context_dict['up_votes'] = Vote.objects.filter(upload=post).filter(vote__gte=1).count()
        context_dict['down_votes'] = Vote.objects.filter(upload=post).filter(vote__lte=-1).count()
        context_dict['comments'] = [c.as_json() for c in Comment.objects.filter(upload=post).filter(
            created_date__lte=timezone.now()).order_by("created_date")]
        if post.uploaded_file.name.endswith(".mp4"):
            context_dict['video'] = True
        else:
            context_dict['video'] = False
        context_dict["user_can_see_nsfw"] = auth_and_older_than_18(request)
    except(ValueError, TypeError, Upload.DoesNotExist):
        print("Exception in user code:")
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
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
                print("Exception in user code:")
                print('-' * 60)
                traceback.print_exc(file=sys.stdout)
                print('-' * 60)
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
        v = Vote.objects.get_or_create(user=user, upload=post)[0]
        v.vote = users_vote
        v.save()
    if ajax == "ajax":
        up_votes = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__gte=1).count()
        down_votes = Vote.objects.filter(upload__hashid=post_hashid).filter(vote__lte=-1).count()
        json_dict = {"ok": True, "up_votes": up_votes, "down_votes": down_votes}
        return HttpResponse(json.dumps(json_dict), content_type="application/json")
    return HttpResponseRedirect(reverse('post', kwargs={'post_hashid': post_hashid}))


# view for search
@csrf_exempt
def search_arg(request, query=""):
    result_list = []
    if request.method == 'POST':
        query_human = request.POST['value']
        query = query_human.strip()
        if query:
            result_list = run_query(query)
    else:
        query_human = query.replace('_', ' ')
        value = query_human.strip()
        if value:
            result_list = run_query(value)
    return render(request, 'imgag/search.html', {'result_list': result_list, 'query_human': query_human})


@login_required
def upload(request):
    user = UserProfile.objects.get(user=request.user)
    cat = Category.objects.get(name=request.POST['category'])
    u = Upload.objects.get_or_create(author=user, header=request.POST['header'], category=cat)[0]
    if 'file' in request.FILES:
        u.uploaded_file = request.FILES['file']
        u.save()
    return home(request)


@login_required
def update_profile_pic(request):
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    user = UserProfile.objects.get(user=request.user)
    if 'profilePic' in request.FILES:
        user.picture = request.FILES['profilePic']
        user.save()
    if 'birth_date' in request.POST:
        try:
            my_datetime = datetime.strptime(request.POST['birth_date'], "%d/%m/%Y")
            user.date_of_birth = pytz.utc.localize(my_datetime)
            print("*************************")
            print(my_datetime)
            print(user.date_of_birth)
            print("*************************")
            user.save()
        except (ValueError, OverflowError):
            print("Exception in user code:")
            print('-' * 60)
            traceback.print_exc(file=sys.stdout)
            print('-' * 60)
    return HttpResponseRedirect(reverse('account'))
