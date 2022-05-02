from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Choose a blog title!'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }