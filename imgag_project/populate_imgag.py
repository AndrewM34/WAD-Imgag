import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'imgag_project.settings')

import django

django.setup()
from datetime import datetime
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User
from imgag.models import UserProfile, Category, Comment, Upload, Vote

from population_data.population import users_list, categories_list, categories_dict


def populate():
    print("Starting populating ImGag. Seat comfortably, please, this is gonna take some time.")

    u, pswd = add_superuser()
    print("Added superuser: '" + u.username + "' and password iiiiiiiiis: '" + pswd + "'")

    users_dict = {}
    for u_dict in users_list:
        username = u_dict["nickname"]
        email = u_dict["email"]
        date_of_birth = u_dict["date_of_birth"]
        path_to_picture = u_dict["path_to_picture"]
        u = add_user(username, email, date_of_birth, path_to_picture)
        users_dict[username] = u
        print("Added user: '" + u.user.username + "'")

    for category_dict in categories_list:
        category_name = category_dict["name"]
        path_to_picture = category_dict["path_to_picture"]
        category = add_category(category_name, path_to_picture)
        print("Added category: '" + category.name + "'")

        uploads_in_category = categories_dict.get(category.name, {})
        for username, users_uploads_in_category in uploads_in_category.items():
            for upload_dict in users_uploads_in_category:
                user = users_dict[username]
                header = upload_dict["header"]
                path_to_file = upload_dict["path_to_file"]
                upload = add_upload(user, category, header, path_to_file)
                print("Added upload: '" + upload.header +
                      "' by '" + upload.author.user.username + "'")

                comments_list = upload_dict["comments"]
                for comment_dict in comments_list:
                    authors_name = comment_dict["authors_name"]
                    author = users_dict[authors_name]
                    text = comment_dict["text"]
                    created_date = comment_dict["created_date"]
                    comment = add_comment(author, upload, text, created_date)
                    print("Added comment: '" + comment.text +
                          "' by '" + comment.author.user.username + "'")


def add_category(name, path_to_picture=None):
    category = Category.objects.get_or_create(name=name)[0]
    if path_to_picture is not None:
        imopen = open(path_to_picture, "rb")
        django_file = File(imopen)
        filename = os.path.basename(path_to_picture)
        category.picture.save(filename, django_file, save=True)
    return category


def add_superuser(username="admin", password="admin123"):
    u = User.objects.get_or_create(username=username)[0]
    u.set_password(password)
    u.is_superuser = True
    u.is_staff = True
    u.save()
    return u, password


def add_user(username, email, date_of_birth, path_to_picture):
    user = User.objects.get_or_create(email=email)[0]
    user.username = username
    user.set_password(username)
    user.save()

    my_datetime = datetime.strptime(date_of_birth, "%b %d %Y")
    profile = \
        UserProfile.objects.get_or_create(user=user,
                                          date_of_birth=timezone.make_aware(my_datetime,
                                                                            timezone.get_current_timezone()))[0]
    if path_to_picture is not None:
        imopen = open(path_to_picture, "rb")
        django_file = File(imopen)
        filename = os.path.basename(path_to_picture)
        profile.picture.save(filename, django_file, save=False)
    profile.save()
    return profile


def add_upload(author, category, header, path_to_file):
    upload = Upload.objects.get_or_create(author=author, category=category, header=header)[0]
    imopen = open(path_to_file, "rb")
    django_file = File(imopen)
    filename = os.path.basename(path_to_file)
    upload.uploaded_file.save(filename, django_file, save=True)
    return upload


def add_comment(author, upload, text, created_date=None):
    comment = Comment.objects.get_or_create(author=author, upload=upload, text=text)[0]
    if created_date is not None:
        created_date = timezone.make_aware(datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S"),
                                           timezone.get_current_timezone())
        comment.created_date = created_date
        comment.save()
    return comment


def add_vote(user, upload, vote=1):
    v = Vote.objects.get_or_create(user=user, upload=upload)[0]
    v.vote = vote
    v.save()
    return v


if __name__ == '__main__':
    populate()
