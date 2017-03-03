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


# Overriding FileSystemStorage class, because Django by default doesn't remove files with the same name => tons of
# same profile pictures, etc.
class OverwriteStorage(FileSystemStorage):
    def _save(self, name, content):
        self.delete(name)
        return super(OverwriteStorage, self)._save(name, content)

    def get_available_name(self, name, max_length=None):
        return name


def upload_to(instance, filename):
    path, prefix = instance.get_upload_dir_and_prefix()
    filename = prefix + filename
    return os.path.join(path, filename)


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
            filename = datetime.utcnow().strftime('%M%S%f') + os.path.basename(self.uploaded_file.name)
            self.uploaded_file.save(filename, django_file, save=True)

    def get_upload_dir_and_prefix(self):
        return os.path.join("uploads", self.author.user.username), self.hashid.hashid

    def __str__(self):
        return self.header

    def __unicode__(self):
        return self.header


class Comment(models.Model):
    author = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    text = models.CharField(max_length=1000)
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


class Vote(models.Model):
    user = models.ForeignKey(UserProfile)
    upload = models.ForeignKey(Upload)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return "User '" + str(self.user) + "' gave '" + str(self.upload) + "': " + str(self.vote)

    def __unicode__(self):
        return "User '" + str(self.user) + "' gave '" + str(self.upload) + "': " + str(self.vote)
