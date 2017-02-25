from django.contrib import admin
from imgag.models import UserProfile, Category, Upload, Comment


class UploadAdmin(admin.ModelAdmin):
    list_display = ('header', 'category', 'author',)


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Upload, UploadAdmin)
admin.site.register(Comment)
