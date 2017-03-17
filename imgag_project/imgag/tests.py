from django.test import TestCase
from imgag.models import Vote, Upload, UserProfile, Comment
from imgag.views import vote
from populate_imgag import populate

from datetime import datetime
from django.utils import timezone
from django.core.files import File
from django.contrib.auth.models import User

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

	def test_upload_has_correct_title(self):
		try:
			testUpload = Upload.objects.all().first()
			response = self.client.get(reverse('post/'+testUpload.hashid))
		except:
			return False

		self.assertIn(testUpload.header, response.content)
