from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from hashid_field import HashidField


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
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

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
    uploaded_file = models.FileField(upload_to='uploads')
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    url_hash = HashidField()


class Comment(models.Model):
    date_stamp = models.DateField(auto_now_add=True)
    user = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    text = models.CharField(max_length=1000)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text
