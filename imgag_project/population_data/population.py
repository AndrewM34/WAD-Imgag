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
        "path_to_picture": os.path.join("population_data", os.path.join("profile_images", "pyotr_img.png"))
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
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "tGWOaPg.png")),
            "header": "Oookay, I think they're having Satan....",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "b4mnxxz.jpg")),
            "header": "I pushed my dog out of the seat so I could sleep during a road-trip, my wife took this picture while I slept.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "A3dtXVj.png")),
            "header": "My friend caught a fish and wanted to take a picture with it, but was to scared to hold it so...",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "0hsql.jpg")),
            "header": "She was waiting in line for 5 minutes.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        }
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
                    "text": "What are you gonna do about it, huh?",
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
                    "text": "I always have A from all subjects.",
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
	"Pyotr": [
        {
            "header": "A star rulez",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "dijkstra.jpg")),
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
            "header": "cant sleep...",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "insomnia.jpg")),
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
            "header": "Love is all there is...",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "find_someone.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Underwood wood be a good president if you get what I mean :^)",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer Kim Chong un",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "When someone tells me I should work...",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "matrix.jpg")),
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
		{
            "header": "Coffee is important...",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "coffee.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "League of legends rulez",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer Mao Tse-Tung",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "No offence...",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "offence.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "whatevs....",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer turmp",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "Oh god!",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "jesus.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Underwood wood be a good president if you get what I mean :^)",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer putin",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "You know it!",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "nut_milk.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Underwood wood be a good president if you get what I mean :^)",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer hillary",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "just CSGO stuff",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "csgo.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Potatos suck...",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I prefer Usama...",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
		{
            "header": "Wow didn't know that :-O",
            "created_date": "2017-2-24 15:30:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "joker.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Does anyone know his true name??",
                    "created_date": "2017-2-25 15:45:17"
                },
                {
                    "authors_name": "herp",
                    "text": "I bet Batman does...",
                    "created_date": "2017-2-25 20:45:37"
                },
            ]
        },
    ],
}

bad_ass_uploads = {
    "Pyotr": [
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "2Nqqtlc.jpg")),
            "header": "What humans could look like if they evolved from other animals",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "5jfz9zB.jpg")),
            "header": "I think that this book series is a bit racist.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
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
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "69UQXUj.jpg")),
            "header": "After 20 minutes of reddit this morning, I've come to this realization",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "7Z32IVK.png")),
            "header": "I can assure you...",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "zoPi7DG.png")),
            "header": "Something tells me Timmy Turner is near by...",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
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
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "xr3rIfu.jpg")),
            "header": "One thing led to another....",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "pBliN8h.jpg")),
            "header": "This guy is walking around campus asking for people's emails so he can send them money",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "h5SiQ.jpg")),
            "header": "I told two girls at the library to be quiet. About an hour later as they left one of them dropped this on my table",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
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
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "OhtPJ.gif")),
            "header": "Every time I get into the shower with my wife",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "aug1ocF.jpg")),
            "header": "+10 armor +20 frost resistance -10 speed",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
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
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "just_another_day_in_maryhill.jpg")),
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
	"herp": [
        {
            "header": "Blows my mind!!!",
            "created_date": "2017-2-14 11:33:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "sort.jpg")),
            "comments": [
                {
                    "authors_name": "herp",
                    "text": "First comment!",
                    "created_date": "2017-2-14 11:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "WHO CARES",
                    "created_date": "2017-2-15 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "burn...",
                    "created_date": "2017-2-15 02:11:11"
                },
            ]
        },
    ],
	"tomator": [
        {
            "header": "Which one was it?",
            "created_date": "2017-3-4 22:40:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "tetris.jpg")),
            "comments": [
                {
                    "authors_name": "BlueDoge",
                    "text": "WoW rulez",
                    "created_date": "2017-3-5 19:41:35"
                },
                {
                    "authors_name": "herp",
                    "text": "CS GO because I have no life whatsoever...",
                    "created_date": "2017-3-5 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "Pac-Man!!!!",
                    "created_date": "2017-3-5 02:11:11"
                },
            ]
        },
    ],
	"Pyotr": [
        {
            "header": "We should really wake up...",
            "created_date": "2017-1-23 22:40:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "water_wifi.jpg")),
            "comments": [
                {
                    "authors_name": "BlueDoge",
                    "text": "true true...",
                    "created_date": "2017-1-24 19:41:35"
                },
                {
                    "authors_name": "Pyotr",
                    "text": "I know right?? We should really do something about it...",
                    "created_date": "2017-1-25 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "No not necessary and global warming is a lie!",
                    "created_date": "2017-1-25 02:11:11"
                },
            ]
        },
		{
            "header": "Take my money!!!",
            "created_date": "2017-3-18 22:40:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "function.png")),
            "comments": [
                {
                    "authors_name": "BlueDoge",
                    "text": "truely deep...",
                    "created_date": "2017-3-18 19:41:35"
                },
                {
                    "authors_name": "herp",
                    "text": "made me think",
                    "created_date": "2017-3-19 01:30:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "not true...",
                    "created_date": "2017-3-19 02:11:11"
                },
            ]
        },
    ],
}

i_cri_evritiem_uploads = {
    "gorilla_boy": [
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "lsoomRq.png")),
            "header": "This is Carter. He knocked on my door to ask if he could have a banana then left.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "bgWINS8.png")),
            "header": "This dry Chicago winter is really taking a toll on my friend's dog",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "iehcWAH.jpg")),
            "header": "Obi-Wan died for our sins",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "JhWo6qp.jpg")),
            "header": "My dog just got out of surgery. I think he might still be high from the anaesthetic.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "header": "Wgenn Ej fand abaud Harambe",
            "created_date": "2017-2-24 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "gorilla_found_out_about_harambe.gif")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I am very sorry for your loss.",
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
	"Pyotr": [
        {
            "header": "anyone here playin' SW Battlefront 1???",
            "created_date": "2017-2-24 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "old_game.jpg")),
            "comments": [
                {
                    "authors_name": "Pyotr",
                    "text": "C mon guys...",
                    "created_date": "2017-2-10 20:41:35"
                },
            ]
        },
		{
            "header": "Yeah... sooo I really did it...",
            "created_date": "2017-1-5 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "winrar.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "I am very sorry for your loss.",
                    "created_date": "2017-1-6 20:41:35"
                },
                {
                    "authors_name": "BlueDoge",
                    "text": "5uk4 b1y4t",
                    "created_date": "2017-1-7 01:45:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "why tho",
                    "created_date": "2017-1-8 05:55:55"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "doesn't make sense...",
                    "created_date": "2017-1-9 14:51:38"
                },
            ]
        },
		{
            "header": "Which one is yours???",
            "created_date": "2017-2-24 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "best_song.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Slipknot - (Sic)",
                    "created_date": "2017-2-25 20:41:35"
                },
                {
                    "authors_name": "darth_procrastinator",
                    "text": "Justin Bieber - Love yourself",
                    "created_date": "2017-2-25 01:45:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "M.O.C. label - Groove street",
                    "created_date": "2017-2-26 05:55:55"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "Steel panther - girl from Oklahoma",
                    "created_date": "2017-3-18 14:51:38"
                },
            ]
        },
		{
            "header": "...we shall see...",
            "created_date": "2017-3-6 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "mc_chicken.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "you probably don't even have a gf...",
                    "created_date": "2017-3-7 20:41:35"
                },
                {
                    "authors_name": "herp",
                    "text": "loser!!!!",
                    "created_date": "2017-3-8 01:45:23"
                },
            ]
        },
		{
            "header": "How can anyone be that stupid???",
            "created_date": "2017-2-24 23:30:05",
            "path_to_file": os.path.join("population_data",
                                         os.path.join("uploads", "nasa_money.jpg")),
            "comments": [
                {
                    "authors_name": "tomator",
                    "text": "Mekka rulez",
                    "created_date": "2017-2-25 20:41:35"
                },
                {
                    "authors_name": "BlueDoge",
                    "text": "Vatican rulez",
                    "created_date": "2017-2-25 01:45:23"
                },
                {
                    "authors_name": "gorilla_boy",
                    "text": "kill them...",
                    "created_date": "2017-2-26 05:55:55"
                },
                {
                    "authors_name": "stoned.stone",
                    "text": "too many people...",
                    "created_date": "2017-3-1 14:51:38"
                },
            ]
        },
    ],
}

next_level_shieeet_uploads = {
    "stoned.stone": [
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "KPVrxlQ.png")),
            "header": "I don't know why, but I digitized that guy's shitty Charmander tattoo",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "b22m35tz2vyx.jpg")),
            "header": "Personal Pizza.",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
        {
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "wp3vDni.jpg")),
            "header": "How does this even hap- Oh...OH!",
            "comments": [],
            "created_date": "2017-3-20 00:06:34"
        },
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
                    "created_date": "2017-3-18 14:50:00"
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
    "BlueDoge": [
        {
            "header": "There is a naked ninja in this image",
            "created_date": "2017-1-11 18:35:05",
            "path_to_file": os.path.join("population_data", os.path.join("uploads", "naked_ninja.jpg")),
            "comments": [
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
