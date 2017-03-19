from django.test import TestCase
from imgag.models import Vote, Upload, UserProfile, Comment
from imgag.views import vote
from populate_imgag import populate
from django.core.urlresolvers import reverse
from datetime import datetime
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.auth import login

import os

# ----------------- TESTS ----------------- #

class TestVoteModel(TestCase):
	def setUp(self):
		populate()

	# test the vote actually saves
	def test_vote_updates(self):
		testUser = UserProfile.objects.all().first()
		testUpload = Upload.objects.all().first()
		testVote = Vote(user=testUser, upload=testUpload)

		testVote.vote = 1 # upboats to the left xD xD eksdee
		testVote.save()
		self.assertEqual(testVote.vote == 1, True)

	# test comments save
	def test_comments(self):
		testComment = Comment.objects.all().first()
		testComment.text = "AEEEAEAEEEAE"
		testComment.save()

		self.assertEqual(testComment.text, "AEEEAEAEEEAE")

	# tests whether a comment is on the correct post
	def test_correct_upload_comment_hashid(self):
		testUpload = Upload.objects.all().first()
		testComment = Comment.objects.filter(upload=testUpload).first()
		self.assertEqual(testComment.upload, testUpload)

	# tests if an upload has the correct title
	def test_upload_has_correct_title(self):
		testUpload = Upload.objects.all().first()
		try:
			response = self.client.get(reverse('post', kwargs={'post_hashid':testUpload.hashid}))
		except:
			print("-"*20+"Could not find an upload")
			self.assertEqual(True, False)

		self.assertIn(bytes(testUpload.header, 'utf-8'), response.content)

	# tests to see if someone can see nsfw content without logging in
	def test_guest_can_see_nsfw(self):
		response = self.client.get(reverse('post', kwargs={'post_hashid':'ZynyW4L'})) # a nsfw post

		self.assertEqual(response.context["user_can_see_nsfw"], False)

	# tests to see if a user under the age of 18 can view nsfw
	def test_under_18_can_see_nsfw(self):
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


		testUser = add_user('ohmycosh', 'ohmycosh@thatdomainsucks.com', 'Jun 1 2005', None)
		login(testcase_user=testUser) # logs in without proper authentication

		response = self.client.get(reverse('post', kwargs={'post_hashid':'ZynyW4L'}))
