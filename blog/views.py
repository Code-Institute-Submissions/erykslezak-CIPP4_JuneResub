from django.shortcuts import render, get_object_or_404
from .models import Post, Tags
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, AddPostForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


def TagsView(request, tags):
    tag_posts = Post.objects.filter(post_tag=tags.replace('-', ' '))
    return render(request, 'tags.html', {'tags': tags.title().replace('-', ' '), 'tag_posts': tag_posts})


def UpvoteView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id_upvote'))
    if post.downvotes.filter(id=request.user.id).exists():
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)
    elif post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def DownvoteView(request, slug):
    post = get_object_or_404(Post, id=request.POST.get('post_id_downvote'))
    if post.upvotes.filter(id=request.user.id).exists():
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)
    elif post.downvotes.filter(id=request.user.id).exists():
        post.downvotes.remove(request.user)
    else:
        post.downvotes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def UpvoteViewIndex(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id_upvote'))
    if post.downvotes.filter(id=request.user.id).exists():
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)
    elif post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)

    return HttpResponseRedirect(reverse('home'))


def DownvoteViewIndex(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id_downvote'))
    if post.upvotes.filter(id=request.user.id).exists():
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)
    elif post.downvotes.filter(id=request.user.id).exists():
        post.downvotes.remove(request.user)
    else:
        post.downvotes.add(request.user)

    return HttpResponseRedirect(reverse('home'))


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        tag_menu = Tags.objects.all()
        tags = super(PostList, self).get_context_data(*args, **kwargs)
        tags["tag_menu"] = tag_menu
        return tags


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

