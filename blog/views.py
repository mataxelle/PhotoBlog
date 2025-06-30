from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from itertools import chain 

from . import forms, models

@login_required
def home_page(request):
    posts = models.Blog.objects.filter(
        Q(contributors__in=request.user.follows.all()) |
        Q(starred=True)
    )

    photos = models.Photo.objects.filter(
        uploader__in=request.user.follows.all()
    ).exclude(blog__in=posts)

    posts_and_photos = sorted(chain(posts, photos), key=lambda instance: instance.date_created, reverse=True)

    paginator = Paginator(posts_and_photos, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'blog/home.html', context=context)

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
    form = forms.PhotoForm()

    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    return render(request, 'blog/photo_upload.html', context={'form': form})

@login_required
@permission_required('blog.add_photo', 'blog.add_blog', raise_exception=True)
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()

    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if any([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.Photo = photo
            blog.save()
            blog.contributors.add(request.user, through_defaults={'contribution': 'Auteur pricipal'})
            return redirect('home')
    
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
    }
    return render(request, 'blog/create_blog_post.html', context=context)

@login_required
def post_view(request, post_id):
    post = get_object_or_404(models.Blog, id=post_id)
    return render(request, 'blog/view_blog_post.html', context={'post': post})

@login_required
@permission_required('blog.change_blog', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(models.Blog, id=post_id)
    edit_form = forms.BlogForm(instance=post)
    delete_form = forms.DeleteBlogForm()

    if request.method == 'POST':
        if 'edit_post' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=post)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        
        if 'delete_post' in request.POST:
            delete_form = forms.DeleteBlogForm(request.POST)
            if delete_form.is_valid():
                post.delete()
                return redirect('home')
            
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'blog/edit_post.html', context=context)

@login_required
@permission_required('blog.add_photo', raise_exception=True)
def multiple_photo_upload(request):
    PhotoFormset = formset_factory(forms.PhotoForm, extra=5)
    formset = PhotoFormset()

    if request.method == 'POST':
        formset = PhotoFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    return render(request, 'blog/multilple_photo_upload.html', {'formset': formset})

@login_required
def follow_users(request):
    form = forms.FollowUsersForm(instance=request.user)
    if request.method == 'POST':
        form = forms.FollowUsersForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'blog/follow_user_form.html', context= {'form': form})

@login_required
def photo_feed(request):
    photos = models.Photo.objects.filter(
        uploader__in=request.user.follows.all()
    ).order_by('-date_created')

    paginator = Paginator(photos, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(request, 'blog/photo_feed.html', context=context)