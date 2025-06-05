from django import forms

from . import models

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