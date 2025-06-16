from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']

class BlogForm(forms.ModelForm):
    edit_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Blog
        fields = ['title', 'Content']

class DeleteBlogForm(forms.Form):
    delete_post = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['follows']