from lxml import html
import requests
import string
from random import randint
import os
from PIL import Image
from StringIO import StringIO

authorsList = ["tomator", "Pyotr", "BlueDoge", "darth_procrastinator", "herp", "gorilla_boy", "stoned.stone"]
extensions = ["png", "jpg", "jpeg", "gif", "gifv"]
url = "https://www.reddit.com/r/funny/search?q=&restrict_sr=on&sort=relevance&t=all"

print "requesting ", url
page = requests.get(url)
tree = html.fromstring(page.content)

# find titles and links to posts, give each a random author
titles = [x for x in tree.xpath('//a[@class="search-title may-blank"]/text()')]
links = [x for x in tree.xpath('//a[@class="search-link may-blank"]/@href')]
authors = [authorsList[randint(0,len(authorsList)-1)] for x in range(len(titles))]

posts = {"tomator":[], "Pyotr":[], "BlueDoge":[], "darth_procrastinator":[], "herp":[], "gorilla_boy":[], "stoned.stone":[]}

print links

out = open('posts', 'w')

if titles != []:
	for link in links:
		if 'a' in link.split('/'): # album, throw away
			i = links.index(link)
			titles.remove(titles[i])
			authors.remove(authors[i])
			links.remove(link)

		if link.split('.')[-1] not in extensions: # link was not a direct image
			link += ".png"

		r = requests.get(link)
		try:
			img = Image.open(StringIO(r.content))
			img.save(link.split('/')[-1])
		except:
			print "could not save as image "+link.split('/')[-1]


	for title in titles:
		author = authors[titles.index(title)]
		filename = links[titles.index(title)].split('/')[-1]
		if filename.split('.')[-1] not in extensions:
			filename += ".png"
		print filename
		posts[author] += [{"header":title, "created_date": "2017-3-20 00:06:34", "path_to_file": filename, "comments":[]}]

	out.write(str(posts))
