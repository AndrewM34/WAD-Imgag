import os

categories_list = [
    {
        "name": "People Are Awesome",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "people_are_awesome.png"))
    },
    {
        "name": "Not So Awesome People",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "not_so_awesome_people.jpg"))
    },
    {
        "name": "Deep",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "deep.jpg"))
    },
    {
        "name": "I Cri Evritiem",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "i_cri_evritiem.jpg"))
    },
    {
        "name": "Next Level Shieeet",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "next_level.jpg"))
    },
    {
        "name": "Crazy",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "crazy.jpg"))
    },
    {
        "name": "Bad Ass",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "badass.jpg"))
    },
    {
        "name": "NSFW",
        "path_to_picture": os.path.join("population_data", os.path.join("category_images", "nsfw.png"))
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
                    "created_date": "2017-3-05 18:32:15"
                },
                {
                    "authors_name": "herp",
                    "text": "No shit, Sherlock",
                    "created_date": "2017-3-05 18:40:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "I don't have to take this.",
                    "created_date": "2017-3-05 20:03:38"
                },
                {
                    "authors_name": "herp",
                    "text": "What are you gonna do about is, huh?",
                    "created_date": "2017-3-05 20:05:05"
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
        {
            "header": "My goat",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "goat.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "That's a nice goat.",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "This is shit...",
                    "created_date": "2017-2-25 20:45:37"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "My goat is better, nerd",
                    "created_date": "2017-2-25 00:45:25"
                },
            ]
        },
        {
            "header": "Spaced out o.O",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "spaced_out.jpeg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Underwood wood be a good president if you get what I mean :^)",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer turmp",
                    "created_date": "2017-2-25 20:45:37"
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
        {
            "header": "Redneck's guide to cutting a bush.",
            "created_date": "2017-2-24 18:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "redneck_chores.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "yee-haw pardner!",
                    "created_date": "2017-2-25 18:47:10"
                },
                {
                    "authors_name": "herp",
                    "text": "that's texas you absolute donut",
                    "created_date": "2017-2-26 21:15:05"
                },
            ]
        },
        {
            "header": "I'm spook'd right now",
            "created_date": "2017-2-24 17:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "spooky.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "omg man u spook'd me too :'( ",
                    "created_date": "2017-2-25 18:41:45"
                },
                {
                    "authors_name": "herp",
                    "text": "fug sake man ur gonna kill someone with that level of spookage",
                    "created_date": "2017-2-26 20:49:11"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "my spook is spookier",
                    "created_date": "2017-2-27 00:50:25"
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
        {
            "header": "What do you guys think of my new ride?",
            "created_date": "2017-2-24 17:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "my_new_ride.jpg")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "damn dude that's super fly",
                    "created_date": "2017-2-25 18:42:45"
                },
                {
                    "authors_name": "tomator",
                    "text": "yes my friend very nice",
                    "created_date": "2017-2-26 20:49:11"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "where can I get one?",
                    "created_date": "2017-2-27 00:50:25"
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
        {
            "header": "Just another day in Maryhill",
            "created_date": "2017-2-24 18:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "just_another_day_in_maryhill.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I can believe this happening",
                    "created_date": "2017-2-24 20:31:15"
                },
                {
                    "authors_name": "herp",
                    "text": "yeah nice repost my man",
                    "created_date": "2017-2-24 20:35:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "Why so salty again?",
                    "created_date": "2017-2-24 20:36:38"
                },
                {
                    "authors_name": "herp",
                    "text": "Stop being you, please.",
                    "created_date": "2017-2-24 20:45:05"
                }
            ]
        },
        {
            "header": "Life imitating art",
            "created_date": "2017-2-24 18:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "life_imitating_art.jpeg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Tru dat :^)",
                    "created_date": "2017-2-24 20:31:15"
                },
                {
                    "authors_name": "herp",
                    "text": "puns should be a bannable offence.",
                    "created_date": "2017-2-24 20:35:21"
                },
                {
                    "authors_name": "tomator",
                    "text": "aaaaa ",
                    "created_date": "2017-2-24 20:36:38"
                },
            ]
        },
        {
            "header": "When your maw says ye canne go oot cause ye pure fucked yer exams like",
            "created_date": "2017-2-24 17:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "waaa.jpg")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "aye pal that's pure shoot",
                    "created_date": "2017-2-25 18:42:45"
                },
                {
                    "authors_name": "tomator",
                    "text": "catch me in viper again lads",
                    "created_date": "2017-2-26 20:49:11"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "I get A1 in all my exams, I don't understand this post.",
                    "created_date": "2017-2-27 00:50:25"
                },
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
            "created_date": "2017-3-13 11:05:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "leaving_oral_exam.gif")),
            "comments": [
                {
                    "authors_name": "Pyotr",
                    "text": "G4g4g4",
                    "created_date": "2017-3-05 11:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Grgrgrgh",
                    "created_date": "2017-3-05 12:11:11"
                },
            ]
        },
        {
            "header": "When bae cooks you ribs :3",
            "created_date": "2017-2-24 17:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "ribs.png")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "tfw no ribs :(",
                    "created_date": "2017-2-25 18:42:45"
                },
                {
                    "authors_name": "tomator",
                    "text": "tfw no bae :(",
                    "created_date": "2017-2-26 20:49:11"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "I wish Freddie was my bae :'(",
                    "created_date": "2017-2-27 00:50:25"
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
                {
                    "authors_name": "stoned.stone",
                    "text": "wtf is wrong with you guy, do you post anything other than gorillas?",
                    "created_date": "2017-3-18 14:51:38"
                },
            ]
        },
    ],
}

next_level_shieeet_uploads = {
    "stoned.stone": [
        {
            "header": "How much for gram xD",
            "created_date": "2017-3-11 23:39:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "how_much_gram.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Admin, please, remove this.",
                    "created_date": "2017-3-13 23:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-3-14 01:45:23"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "Dude chill",
                    "created_date": "2017-3-14 05:55:55"
                },
            ]
        },
        {
            "header": "When I come home drunk and parents are awake",
            "created_date": "2017-3-07 23:59:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "when_i_come_home_drunk.mp4")),
            "comments": [
                {
                    "authors_name": "Pyotr",
                    "text": "G4g4g4, s0m3 v0dk4 f0r m3 pl34s3",
                    "created_date": "2017-3-14 02:43:23"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "K bro xD",
                    "created_date": "2017-3-14 05:59:59"
                },
            ]
        },
        {
            "header": "Me at viper",
            "created_date": "2017-3-11 23:39:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "me_at_viper.gif")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "lookin' good, my man",
                    "created_date": "2017-3-13 23:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "I'm more of a hive kinda guy",
                    "created_date": "2017-3-14 01:45:23"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "Hive is literally the worst. You must be high to think that viper is worse than Hive.",
                    "created_date": "2017-3-14 05:55:55"
                },
                {
                    "authors_name": "herp",
                    "text": "old viper was better tho",
                    "created_date" : "2017-3-18 14:50:00"
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
