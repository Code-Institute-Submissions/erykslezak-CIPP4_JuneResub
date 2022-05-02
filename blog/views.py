from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.generic import CreateView, ListView, DetailView

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(DetailView):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )


class AddPost(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'