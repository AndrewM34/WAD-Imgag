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
        {
            "name": "Hot",
        },
        {
            "name": "Trending",
        },
        {
            "name": "People are awesome"
        },
        {
            "name": "NFSW"
        },
    ]
    users = [
        {
            "nickname": "tomator",
            "email": "tomator@google.com",
            "date_of_birth": "Jun 1 1997",
            "path_to_picture": os.path.join("population_data", os.path.join("profile_pictures", "tomator.png"))
        },
    ]

    people_are_awesome_uploads = {
        "tomator": {
            "header": "This is crazy, right?",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "crazy_right")),
            "upvotes": 5,
            "downvotes": 10
        },
    }

    hot_uploads = [
        {

        }
    ]
    categories = [
        {
            "People are awesome": people_are_awesome_uploads,
        }
    ]
    for user in users:
        username = user["nickname"]
        email = user["email"]
        date_of_birth = user["date_of_birth"]
        path_to_picture = user["path_to_picture"]
        add_user(username, email, date_of_birth, path_to_picture)


def add_category(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_user(name, email, date_of_birth,
             path_to_picture=os.path.join("population_data", os.path.join("profile_pictures", "default.png"))):
    user = User.objects.get_or_create(email=email)[0]
    user.username = name
    user.save()

    my_datetime = datetime.strptime(date_of_birth, "%b %d %Y")
    profile = \
        UserProfile.objects.get_or_create(user=user,
                                          date_of_birth=timezone.make_aware(my_datetime,
                                                                            timezone.get_current_timezone()))[0]

    print(profile)

    imopen = open(path_to_picture, "rb")
    django_file = File(imopen)
    filename = os.path.join(name, os.path.basename(path_to_picture))
    profile.picture.save(filename, django_file, save=True)

    print(UserProfile.objects.all())


if __name__ == '__main__':
    print("Starting populating ImGag. Seat comfortably, please, this is gonna take some time.")
    populate()
