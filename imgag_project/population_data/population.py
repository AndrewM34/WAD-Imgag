import os

categories_list = [
    {
        "name": "People Are Awesome",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "people_are_awesome.png"))
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

superusers_list = [
    {
        "nickname": "admin",
        "password": "admin123"
    },
]

users_list = [
    {
        "nickname": "tomator",
        "email": "tomator@google.com",
        "date_of_birth": "Jun 1 1997",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "tomator.png"))
    },
    {
        "nickname": "Pyotr",
        "email": "pyotr.pyotrovic@yandex.com",
        "date_of_birth": "Dec 31 1993",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "pyotr.png"))
    },
    {
        "nickname": "BlueDoge",
        "email": "dogeswin@google.com",
        "date_of_birth": "May 30 1990",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "blue_doge.jpg"))
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
    {
        "nickname": "gorilla_boy",
        "email": "love.grod@gorill.az",
        "date_of_birth": "Jun 10 2009",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "gorilla_boy.jpg"))
    },
    {
        "nickname": "stoned.stone",
        "email": "rocky.rock@tratra.tv",
        "date_of_birth": "May 10 1993",
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "stoned_stone.png"))
    },
]

people_are_awesome_uploads = {
    "BlueDoge": [
        {
            "header": "Amazing math skills",
            "created_date": "2017-3-13 19:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "rest_15_percent.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I think it does not sum to 100 percent.",
                    "created_date": "2017-3-14 20:31:15"
                },
                {
                    "authors_name": "herp",
                    "text": "No shit, Sherlock",
                    "created_date": "2017-3-14 20:35:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "Why are you like this?",
                    "created_date": "2017-3-14 20:36:38"
                },
                {
                    "authors_name": "herp",
                    "text": "GTFO",
                    "created_date": "2017-3-14 20:45:05"
                }
            ]
        },
    ],
    "tomator": [
        {
            "header": "My Python skill",
            "created_date": "2017-3-13 19:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "microwave_python.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "This a joke - Python is a programming language and also a snake.",
                    "created_date": "2017-3-15 18:32:15"
                },
                {
                    "authors_name": "herp",
                    "text": "No shit, Sherlock",
                    "created_date": "2017-3-15 18:40:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "I don't have to take this.",
                    "created_date": "2017-3-15 20:03:38"
                },
                {
                    "authors_name": "herp",
                    "text": "What are you gonna do about is, huh?",
                    "created_date": "2017-3-15 20:05:05"
                }
            ]
        },
        {
            "header": "Me doing exams",
            "created_date": "2017-3-12 17:30:03",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "doing_exams_like_a_boss.gif")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I always have A from all subject.",
                    "created_date": "2017-3-12 18:32:15"
                },
                {
                    "authors_name": "herp",
                    "text": "fking nerd",
                    "created_date": "2017-3-12 18:40:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "I am just clever, don't be rude please.",
                    "created_date": "2017-3-13 20:03:38"
                },
                {
                    "authors_name": "herp",
                    "text": "Bebeee, are you gonna cry?",
                    "created_date": "2017-3-13 20:05:05"
                }
            ]
        },
    ],
}

bad_ass_uploads = {
    "Pyotr": [
        {
            "header": "M3 g4ing 14jk 4 b055 m4j c0mr4d3",
            "created_date": "2017-2-24 15:30:05",
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
    "gorilla_boy": [
        {
            "header": "Ma hairrow",
            "created_date": "2017-2-24 20:30:15",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "grod_flash.jpg")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "Flash got what he deserved.",
                    "created_date": "2017-1-25 20:45:37"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-2-25 01:45:23"
                },
            ]
        },
        {
            "header": "Na van givz ma fyngr",
            "created_date": "2017-2-24 00:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "gorilla_giving_finger.mp4")),
            "comments": [
                {
                    "authors_name": "BlueDoge",
                    "text": "Hahah, duuude.",
                    "created_date": "2017-2-10 19:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "R45h B",
                    "created_date": "2017-2-25 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Aaaargh ugh ugh",
                    "created_date": "2017-2-25 06:33:33"
                },
            ]
        },
    ]
}

not_so_awesome_people_uploads = {
    "darth_procrastinator": [
        {
            "header": "Me running from responsibilities",
            "created_date": "2017-2-24 17:30:05",
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
            "created_date": "2017-2-24 18:30:05",
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
    "gorilla_boy": [
        {
            "header": "Ma frrend yz pyg",
            "created_date": "2017-2-24 19:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "gorilla_nose_picking.gif")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Well, this is not very nice.",
                    "created_date": "2017-2-10 20:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-2-25 01:45:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Ugh",
                    "created_date": "2017-2-25 05:55:55"
                },
            ]
        },
    ],
}

crazy_uploads = {
    "tomator": [
        {
            "header": "This is crazy, right?",
            "created_date": "2017-2-24 18:30:05",
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

deep_uploads = {
    "gorilla_boy": [
        {
            "header": "Wgenn Ej zii cilrn (puurr Harambe)",
            "created_date": "2017-2-23 22:40:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "gorilla_im_outta_here.gif")),
            "comments": [
                {
                    "authors_name": "BlueDoge",
                    "text": "We will never forget",
                    "created_date": "2017-2-10 19:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "R45h B, H4r4mb3",
                    "created_date": "2017-2-25 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Aaaargh aaaarghghh",
                    "created_date": "2017-2-25 02:11:11"
                },
            ]
        },
    ],
    "darth_procrastinator": [
        {
            "header": "After an oral exam",
            "created_date": "2017-3-23 11:05:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "leaving_oral_exam.gif")),
            "comments": [
                {
                    "authors_name": "Pyotr",
                    "text": "G4g4g4",
                    "created_date": "2017-3-25 11:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Grgrgrgh",
                    "created_date": "2017-3-25 12:11:11"
                },
            ]
        },
    ],
}

i_cri_evritiem_uploads = {
    "gorilla_boy": [
        {
            "header": "Wgenn Ej fand abaud Harambe",
            "created_date": "2017-2-24 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "gorilla_found_out_about_harambe.gif")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I am very sorry for you loss.",
                    "created_date": "2017-2-10 20:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-2-25 01:45:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Aaaargh",
                    "created_date": "2017-2-25 05:55:55"
                },
            ]
        },
    ],
}

next_level_shieeet_uploads = {
    "stoned.stone": [
        {
            "header": "How much for gram xD",
            "created_date": "2017-3-21 23:39:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "how_much_gram.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Admin, please, remove this.",
                    "created_date": "2017-3-23 23:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-3-24 01:45:23"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "Dude chill",
                    "created_date": "2017-3-24 05:55:55"
                },
            ]
        },
        {
            "header": "When I come home drunk and parents are awake",
            "created_date": "2017-3-17 23:59:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "when_i_come_home_drunk.mp4")),
            "comments": [
                {
                    "authors_name": "Pyotr",
                    "text": "G4g4g4, s0m3 v0dk4 f0r m3 pl34s3",
                    "created_date": "2017-3-24 02:43:23"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "K bro xD",
                    "created_date": "2017-3-24 05:59:59"
                },
            ]
        },
    ],
}

nsfw_uploads = {
    "tomator": [
        {
            "header": "So after seeing Logan I have decided for a new haircut.",
            "created_date": "2017-3-11 18:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "i_look_like_wolverine.jpg")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "LOL",
                    "created_date": "2017-3-11 20:35:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "What?",
                    "created_date": "2017-3-11 20:36:38"
                },
                {
                    "authors_name": "herp",
                    "text": "Ahahaha",
                    "created_date": "2017-3-11 20:45:05"
                }
            ]
        },
    ],
}

categories_dict = {
    "People Are Awesome": people_are_awesome_uploads,
    "Bad Ass": bad_ass_uploads,
    "Not So Awesome People": not_so_awesome_people_uploads,
    "Crazy": crazy_uploads,
    "Deep": deep_uploads,
    "I Cri Evritiem": i_cri_evritiem_uploads,
    "Next Level Shieeet": next_level_shieeet_uploads,
    "NSFW": nsfw_uploads,
}
