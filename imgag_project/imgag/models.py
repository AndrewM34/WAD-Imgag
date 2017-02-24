from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from hashid_field import HashidAutoField


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateTimeField()
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=140, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Upload(models.Model):
    header = models.CharField(max_length=140)
    user = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    file = models.FileField(upload_to='uploads', blank=False)
    upVote = models.IntegerField(default=0)
    downVote = models.IntegerField(default=0)
    url_hash = HashidAutoField()

class Comment(models.Model):
    date_stamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text



