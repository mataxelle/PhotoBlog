from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User
from blog.models import Photo, Blog

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'date_created', 'uploader')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'author')

admin.site.register(User, UserAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Blog, BlogAdmin)
