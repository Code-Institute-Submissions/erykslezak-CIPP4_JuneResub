from .models import Comment, Post, Tags, UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from cloudinary.forms import CloudinaryFileField

tags = Tags.objects.all().values_list('name', 'name')

tags_list = []

for tag in tags:
    tags_list.append(tag)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_tag', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a post title'}),
            'post_tag': forms.Select(choices=tags_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_tag', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a post title'}),
            'post_tag': forms.Select(choices=tags_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('user_bio', 'user_image')
        widgets = {
            'user_bio': forms.Textarea(attrs={'class': 'form-control user-form'}),
        }


class EditUserForm(forms.ModelForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control user-form'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control user-form'}),
        }