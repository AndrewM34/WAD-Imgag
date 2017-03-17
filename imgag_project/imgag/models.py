from __future__ import unicode_literals

import os
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from hashid_field import HashidAutoField
from datetime import datetime
from django.utils import timezone
from django.core.files import File
from django.conf import settings

from registration.signals import user_registered


# Overriding FileSystemStorage class, because Django by default doesn't remove files with the same name => tons of
# same profile pictures, etc.
class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        self.delete(name)
        # Delete default file if there was such
        filename, extension = os.path.splitext(os.path.basename(name))
        hashid = filename[:-10]
        self.delete(os.path.join(os.path.dirname(name), hashid + "defaultdef.png"))
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name


def upload_to(instance, filename):
    path, prefix = instance.get_upload_dir_and_prefix()
    filename, extension = os.path.splitext(filename)
    # There are exactly 10 characters between extension and after hashid
    filename = (filename * (10 // len(filename) + 1))[:10]
    filename = prefix + filename + extension
    return os.path.join(path, filename)

def user_registered_callback(sender,user,request,**kwargs):
	print ("got hereeeeeeeeeeeee")
	profile = UserProfile(user=user)
	profile.save()

user_registered.connect(user_registered_callback)

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    date_of_birth = models.DateTimeField()
    picture = models.ImageField(upload_to=upload_to, storage=OverwriteStorage(),
                                default=os.path.join("default",
                                                     os.path.join("profile_images", "default.png")))

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.date_of_birth:
            self.date_of_birth = timezone.make_aware(datetime.now(),
                                                    timezone.get_current_timezone())
        if os.path.basename(self.picture.name) == "default.png":
            imopen = open(os.path.join(settings.MEDIA_ROOT, self.picture.name), "rb")
            django_file = File(imopen)
            old_filename, extension = os.path.splitext(self.picture.name)
            filename = self.user.username + extension
            self.picture.save(filename, django_file, save=False)
        super(UserProfile, self).save(*args, **kwargs)

    def get_upload_dir_and_prefix(self):
        return os.path.join("profile_images", self.user.username), ""


class Category(models.Model):
    name = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(unique=True)
    picture = models.ImageField(upload_to=upload_to, storage=OverwriteStorage(),
                                default=os.path.join("default",
                                                     os.path.join("uploads", "default.png")))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if os.path.basename(self.picture.name) == "default.png":
            imopen = open(os.path.join(settings.MEDIA_ROOT, self.picture.name), "rb")
            django_file = File(imopen)
            filename = os.path.basename(self.picture.name)
            self.picture.save(filename, django_file, save=False)
        super(Category, self).save(*args, **kwargs)

    def get_upload_dir_and_prefix(self):
        return os.path.join("category_images", self.slug), ""

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def as_json(self):
        return dict(name=self.name,
                    slug=str(self.slug),
                    picture_url=self.picture.url)


class Upload(models.Model):
    header = models.CharField(max_length=140)
    author = models.ForeignKey(UserProfile)
    category = models.ForeignKey(Category)
    uploaded_file = models.FileField(upload_to=upload_to, storage=OverwriteStorage(),
                                     default=os.path.join("default",
                                                          os.path.join("uploads", "default.png")))
    hashid = HashidAutoField(primary_key=True)
    created_date = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.make_aware(datetime.now(),
                                                    timezone.get_current_timezone())
        super(Upload, self).save(*args, **kwargs)

        if os.path.basename(self.uploaded_file.name) == "default.png":
            imopen = open(os.path.join(settings.MEDIA_ROOT, self.uploaded_file.name), "rb")
            django_file = File(imopen)
            filename = os.path.basename(self.uploaded_file.name)
            self.uploaded_file.save(filename, django_file, save=True)

    def get_upload_dir_and_prefix(self):
        return os.path.join("uploads", self.author.user.username), self.hashid.hashid

    def __str__(self):
        return self.header

    def __unicode__(self):
        return self.header

    def as_json(self):
        return dict(author=str(self.author),
                    header=str(self.header),
                    category=str(self.category),
                    created_date=self.created_date.strftime("%Y-%m-%d %H:%M"),
                    upload_url=str(self.uploaded_file.url),
                    hashid=str(self.hashid.hashid),
                    is_video=str(self.uploaded_file.name).endswith(".mp4"))


class Comment(models.Model):
    author = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    text = models.CharField(max_length=200)
    created_date = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.created_date:
            self.created_date = timezone.make_aware(datetime.now(),
                                                    timezone.get_current_timezone())
        super(Comment, self).save(*args, **kwargs)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text

    def as_json(self):
        return dict(author=str(self.author),
                    author_image_url=str(self.author.picture.url),
                    upload_hashid=self.upload.hashid.hashid,
                    text=str(self.text),
                    created_date=self.created_date.strftime("%Y-%m-%d %H:%M"))


class Vote(models.Model):
    user = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return "User '" + str(self.user) + "' gave '" + str(self.upload) + "': " + str(self.vote)

    def __unicode__(self):
        return "User '" + str(self.user) + "' gave '" + str(self.upload) + "': " + str(self.vote)
