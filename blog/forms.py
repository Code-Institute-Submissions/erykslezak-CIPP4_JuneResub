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


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_tag', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Choose a post title'}),
            'post_tag': forms.Select(choices=tags_list, attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_image = CloudinaryFileField(required=False)
    user_bio = forms.CharField(max_length=100,required=False,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'user_image', 'user_bio')
        # fields = ('username', 'first_name', 'last_name')