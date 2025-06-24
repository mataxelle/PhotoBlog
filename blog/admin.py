from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User
from blog.models import Photo, Blog, BlogContributor

class CustomUser(UserAdmin):
    list_display = ('username', 'role')

    # Ajoute les champs personnalisés dans la page de modification
    fieldsets = UserAdmin.fieldsets + (
        ('Informations supplémentaires', {
            'fields': ('role', 'follows'),
        }),
    )

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'date_created', 'uploader')

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')

class BlogContributorAdmin(admin.ModelAdmin):
    list_display = ('blog', 'contributor', 'contribution')

admin.site.register(User, CustomUser)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogContributor, BlogContributorAdmin)
