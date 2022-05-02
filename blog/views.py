from django.shortcuts import render, get_object_or_404
from .models import Post
from django.urls import reverse_lazy
from .forms import CommentForm, AddPostForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class UserPostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'user_posts.html'



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
    form_class = AddPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'slug', 'content']


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

