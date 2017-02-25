from django.contrib import admin
from imgag.models import UserProfile, Category, Upload, Comment

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Upload)
admin.site.register(Comment)