import os

categories_list = [
    {
        "name": "People Are Awesome",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_pictures", "people_are_awesome.png"))
    },
    {
        "name": "Not So Awesome People",
        "path_to_picture": None
    },
    {
        "name": "Deep",
        "path_to_picture": None
    },
    {
        "name": "I Cri Evritiem",
        "path_to_picture": None
    },
    {
        "name": "Next Level Shieeet",
        "path_to_picture": None
    },
    {
        "name": "Crazy",
        "path_to_picture": None
    },
    {
        "name": "Bad Ass",
        "path_to_picture": None
    },
    {
        "name": "NSFW",
        "path_to_picture": None
    },
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

bad_ass_uploads = {
    "Pyotr": [
        {
            "header": "M3 g4ing 14jk 4 b055 m4j c0mr4d3",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "me_going_with_bag.mp4")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Don't act as you would be tough, I know you are a good guy, Pyotr.",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "This is shit...",
                    "created_date": "2017-2-25 20:45:37"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "R45h B, 5uk4 b1y4t",
                    "created_date": "2017-2-25 00:45:25"
                },
            ]
        },
    ],
}

not_so_awesome_people_uploads = {
    "darth_procrastinator": [
        {
            "header": "Me running from responsibilities",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "me_running_from_responsibilities.mp4")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Very nice post, dear Procrastinator. I feel with you, my friend.",
                    "created_date": "2017-2-25 18:41:45"
                },
                {
                    "authors_name": "herp",
                    "text": "This is shit...",
                    "created_date": "2017-2-26 20:49:11"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "R45h B, 1 s33 m4js31f 1n th15, c0mr4d3, 5uk4 b1y4t",
                    "created_date": "2017-2-27 00:50:25"
                },
            ]
        },
        {
            "header": "When someone does a shitty work for me.",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "i_wanted_to_do_it.mp4")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I have not enjoyed this post so much, Mr Procrastinator. But keep up!",
                    "created_date": "2017-2-25 18:47:10"
                },
                {
                    "authors_name": "herp",
                    "text": "This is shit...",
                    "created_date": "2017-2-26 21:15:05"
                },
            ]
        },
    ],
}

categories_dict = {
    "People Are Awesome": people_are_awesome_uploads,
    "Bad Ass": bad_ass_uploads,
    "Not So Awesome People": not_so_awesome_people_uploads,
}
