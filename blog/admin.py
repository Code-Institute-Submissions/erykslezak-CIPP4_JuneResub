'''
Imports the relevant packages
'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import Post, Comment, Tags, UserProfile


class UserProfileInline(admin.TabularInline):
    '''
    Part of extending UserProfile model to the all auth User model.
    '''
    model = UserProfile


class UserAdmin(DjangoUserAdmin):
    '''
    Inlines the UserProfile model to User section
    '''
    inlines = [UserProfileInline, ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tags)
