from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Choose a post title!'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }