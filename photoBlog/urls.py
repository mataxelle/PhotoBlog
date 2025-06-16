"""
URL configuration for photoBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path
import authentication.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('', LoginView.as_view(
        template_name = 'authentication/login.html',
        redirect_authenticated_user = True
        ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'
        ), name='password_change'),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'
        ), name='password_change_done'),
    path('home/', blog.views.home_page, name='home'),
    path('photo/upload/', blog.views.photo_upload, name='photo_upload'),
    path('profile-photo/upload/', authentication.views.profile_photo_upload, name='profile_photo_upload'),
    path('blog/create/', blog.views.blog_and_photo_upload, name='blog_create'),
    path('blog/<int:post_id>/', blog.views.post_view, name='post_view'),
    path('blog/<int:post_id>/edit/', blog.views.edit_post, name='edit_post'),
    path('photo/multiple-upload/', blog.views.multiple_photo_upload, name='multiple_photo_upload'),
    path('follow_users/', blog.views.follow_users, name='follow_users'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
