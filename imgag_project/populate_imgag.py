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
    # do = datetime.strptime(users[0].get("date_of_birth"), "%b %d %Y")
    category = [
        "People are awesome",
        "Deep",
        "I Cri Evritiem",
        "Crazy",
        "Next level shieeet",
        "NSFW",
    ]
    users_dict = [
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
                "downvotes": 10
            },
        ],
    }

    hot_uploads = [
        {

        }
    ]
    categories_dict = {
        "People are awesome": people_are_awesome_uploads,
    }

    categories = {}

    for category_name, uploads_in_category in categories_dict.items():
        c = add_category(category_name)
        print("Added category: " + c.name)
        categories[c] = uploads_in_category

    for user in users_dict:
        username = user["nickname"]
        email = user["email"]
        date_of_birth = user["date_of_birth"]
        path_to_picture = user["path_to_picture"]
        u = add_user(username, email, date_of_birth, path_to_picture)
        print("Added user: " + u.user.username)

        for category, uploads_in_category in categories.items():
            users_uploads = uploads_in_category.get(username, {})
            for upload in users_uploads:
                header = upload["header"]
                path_to_file = upload["path_to_file"]
                up_votes = upload["upvotes"]
                down_votes = upload["downvotes"]
                up = add_upload(u, category, header, path_to_file, up_votes, down_votes)
                print("Added upload: " + up.header)


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


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


def add_upload(user, category, header, path_to_file, up_votes=0, down_votes=0):
    upload = Upload.objects.get_or_create(user=user, category=category, header=header, up_votes=up_votes,
                                          down_votes=down_votes)[0]
    imopen = open(path_to_file, "rb")
    django_file = File(imopen)
    filename = os.path.join(user.user.username,
                            upload.hashid.hashid + os.path.basename(path_to_file))
    upload.uploaded_file.save(filename, django_file, save=True)
    return upload


def add_comment():
    pass


if __name__ == '__main__':
    print("Starting populating ImGag. Seat comfortably, please, this is gonna take some time.")
    populate()
