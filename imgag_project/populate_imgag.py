import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'imgag_project.settings')

import django

django.setup()
from datetime import datetime
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User
from imgag.models import UserProfile, Category, Comment, Upload


def populate():
    categories_list = [
        "People are awesome",
        "Deep",
        "I Cri Evritiem",
        "Crazy",
        "Next level shieeet",
        "NSFW",
    ]
    users_list = [
        {
            "nickname": "tomator",
            "email": "tomator@google.com",
            "date_of_birth": "Jun 1 1997",
            "path_to_picture": os.path.join("population_data", os.path.join("profile_pictures", "tomator.png"))
        },
        {
            "nickname": "Pyotr",
            "email": "pyotr.pyotrovic@yandex.com",
            "date_of_birth": "Dec 31 1993",
            "path_to_picture": os.path.join("population_data", os.path.join("profile_pictures", "pyotr.png"))
        },
        {
            "nickname": "BlueDoge",
            "email": "dogeswin@google.com",
            "date_of_birth": "May 30 1990",
            "path_to_picture": os.path.join("population_data", os.path.join("profile_pictures", "blue_doge.jpg"))
        },
        {
            "nickname": "darth_procrastinator",
            "email": "red@saber.fr",
            "date_of_birth": "Jun 1 1985",
            "path_to_picture": None
        },
        {
            "nickname": "herp",
            "email": "herp@amigo.es",
            "date_of_birth": "Jun 1 2005",
            "path_to_picture": None
        },
    ]

    people_are_awesome_uploads = {
        "tomator": [
            {
                "header": "This is crazy, right?",
                "path_to_file": os.path.join("population_data", os.path.join("uploads", "crazy_right.png")),
                "upvotes": 5,
                "downvotes": 10,
                "comments": [
                    {
                        "authors_name": "tomator",
                        "text": "Hope you'll like this guys <3",
                        "created_date": "2017-2-24 20:31:15"
                    },
                    {
                        "authors_name": "herp",
                        "text": "This is shit...",
                        "created_date": "2017-2-24 20:35:21"
                    },
                    {
                        "authors_name": "tomator",
                        "text": "Why so salty?",
                        "created_date": "2017-2-24 20:36:38"
                    },
                    {
                        "authors_name": "herp",
                        "text": "I don't like you.",
                        "created_date": "2017-2-24 20:45:05"
                    }
                ]
            },
        ],
    }

    categories_dict = {
        "People are awesome": people_are_awesome_uploads,
    }

    users_dict = {}
    for u_dict in users_list:
        username = u_dict["nickname"]
        email = u_dict["email"]
        date_of_birth = u_dict["date_of_birth"]
        path_to_picture = u_dict["path_to_picture"]
        u = add_user(username, email, date_of_birth, path_to_picture)
        users_dict[username] = u
        print("Added user: '" + u.user.username + "'")

    for category_name in categories_list:
        category = add_category(category_name)
        print("Added category: '" + category.name + "'")

        uploads_in_category = categories_dict.get(category.name, {})
        for username, users_uploads_in_category in uploads_in_category.items():
            for upload_dict in users_uploads_in_category:
                user = users_dict[username]
                header = upload_dict["header"]
                path_to_file = upload_dict["path_to_file"]
                up_votes = upload_dict["upvotes"]
                down_votes = upload_dict["downvotes"]
                upload = add_upload(user, category, header, path_to_file, up_votes, down_votes)
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


def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    return category


def add_user(name, email, date_of_birth, path_to_picture):
    if path_to_picture is not None:
        return _add_user(name, email, date_of_birth, path_to_picture)
    else:
        return _add_user(name, email, date_of_birth)


def _add_user(name, email, date_of_birth,
              path_to_picture=os.path.join("population_data", os.path.join("profile_pictures", "default.png"))):
    user = User.objects.get_or_create(email=email)[0]
    user.username = name
    user.save()

    my_datetime = datetime.strptime(date_of_birth, "%b %d %Y")
    profile = \
        UserProfile.objects.get_or_create(user=user,
                                          date_of_birth=timezone.make_aware(my_datetime,
                                                                            timezone.get_current_timezone()))[0]
    imopen = open(path_to_picture, "rb")
    django_file = File(imopen)
    filename = os.path.join(name, os.path.basename(path_to_picture))
    profile.picture.save(filename, django_file, save=True)
    return profile


def add_upload(author, category, header, path_to_file, up_votes=0, down_votes=0):
    upload = Upload.objects.get_or_create(author=author, category=category, header=header, up_votes=up_votes,
                                          down_votes=down_votes)[0]
    imopen = open(path_to_file, "rb")
    django_file = File(imopen)
    filename = os.path.join(author.user.username,
                            upload.hashid.hashid + os.path.basename(path_to_file))
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


if __name__ == '__main__':
    print("Starting populating ImGag. Seat comfortably, please, this is gonna take some time.")
    populate()
