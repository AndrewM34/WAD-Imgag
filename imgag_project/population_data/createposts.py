from lxml import html
import requests
import string
from random import randint
import os
from PIL import image
from StringIO import StringIO

authorsList = ['tomator', 'Pyotr', 'BlueDoge', 'darth_procrastinator', 'herp', 'gorilla_boy', 'stoned.stone']

url = "https://www.reddit.com/r/funny/search?q=&restrict_sr=on&sort=relevance&t=all"

print "requesting ", url
page = requests.get(url)
tree = html.fromstring(page.content)

# find titles and links to posts, give each a random author
titles = [x for x in tree.xpath('//a[@class="search-title may-blank"]/text()')]
links = [x for x in tree.xpath('//a[@class="search-link may-blank"]/@href')]
authors = [authorsList[randint(0,len(authorsList)-1)] for x in range(len(titles))]

posts = {'tomator':[], 'Pyotr':[], 'BlueDoge':[], 'darth_procrastinator':[], 'herp':[], 'gorilla_boy':[], 'stoned.stone':[]}

print titles
print links

for link in links:
	r = requests.get(link)
	print link
	img = Image.open(StringIO(r.content))
	img.save()


for title in titles:
	author = authors[titles.index(title)]
	filename = ''
	posts[author] += [{"header":title, "created_date": "2017-3-20 00:06:34", "path_to_file": os.path.join("uploads", filename), "comments":[]}]

print '-'*60

print posts
