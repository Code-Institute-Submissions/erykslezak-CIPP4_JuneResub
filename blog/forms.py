'''
Imports the relevant packages
'''
from .models import Comment, Post, Tags, UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from cloudinary.forms import CloudinaryFileField
import os

tags = Tags.objects.all().values_list('name', 'name')

tags_list = []

# A loop that adds new tags to current ones
for tag in tags:
    tags_list.append(tag)


class CommentForm(forms.ModelForm):
    '''
    Comment form which consists only of body field.
    '''
    class Meta:
        '''
        Necessary comment fields
        '''
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    '''
    Add new post form
    '''
    class Meta:
        '''
        Necessary post fields
        '''
        model = Post
        fields = ('title', 'post_tag', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Choose a post title'}),
            'post_tag': forms.Select(choices=tags_list,
                                     attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class EditPostForm(forms.ModelForm):
    '''
    Edit post form
    '''
    class Meta:
        '''
        Necessary fields in order to edit the post
        '''
        model = Post
        fields = ('title', 'post_tag', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Choose a post title'}),
            'post_tag': forms.Select(choices=tags_list,
                                     attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditUserProfileForm(forms.ModelForm):
    '''
    Edit user profile form
    '''
    user_image = forms.ImageField(label=('User Image'), required=False,
                                  widget=forms.FileInput)
    remove_image = forms.BooleanField(required=False)

    class Meta:
        '''
        Fields for user to edit as per UserProfile model extension
        '''
        model = UserProfile
        fields = ('user_bio', 'user_image')
        widgets = {
            'user_bio': forms.Textarea(attrs={'class':
                                              'form-control user-form'}),
        }

    # function that lets user 'delete' their current image
    # and go back to default one
    def save(self, commit=True):
        instance = super(EditUserProfileForm, self).save(commit=False)
        if self.cleaned_data.get('remove_image'):
            try:
                os.unlink(instance.user_image.url)
            except OSError:
                pass
            instance.user_image = ('https://res.cloudinary.com/craity/image/'
                                   'upload/v1651927366/CIPP4/'
                                   'default_profile.png')
        if commit:
            instance.save()
        return instance


class EditUserForm(forms.ModelForm):
    '''
    Edit user form
    '''
    password = None

    class Meta:
        '''
        Fields from the All auth User model
        '''
        model = User
        fields = ('first_name', 'last_name')
        widgets = {
            'first_name': forms.TextInput(attrs={'class':
                                                 'form-control user-form'}),
            'last_name': forms.TextInput(attrs={'class':
                                                'form-control user-form'}),
        }
