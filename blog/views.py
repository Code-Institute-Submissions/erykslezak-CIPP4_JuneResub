'''
Imports the relevant packages
'''
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import (CreateView, ListView, DetailView,
                                  UpdateView, DeleteView)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tags, UserProfile, Comment, User
from .forms import (CommentForm, PostForm, EditUserProfileForm,
                    EditUserForm, EditPostForm)


def tags_view(request, tags):
    '''
    Function for sorting posts by their tags
    '''
    tag_posts = Post.objects.filter(post_tag=tags.replace('-', ' '))
    return render(request, 'tags.html', {'tags': tags.title()
                  .replace('-', ' '), 'tag_posts': tag_posts})


def upvote_view(request, slug):
    '''
    Function for upvoting posts
    '''
    post = get_object_or_404(Post, id=request.POST.get('post_id_upvote'))
    if post.downvotes.filter(id=request.user.id).exists():
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)
    elif post.upvotes.filter(id=request.user.id).exists():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)

    return redirect(request.META['HTTP_REFERER'])


def downvote_view(request, slug):
    '''
    Function for downvoting posts
    '''
    post = get_object_or_404(Post, id=request.POST.get('post_id_downvote'))
    if post.upvotes.filter(id=request.user.id).exists():
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)
    elif post.downvotes.filter(id=request.user.id).exists():
        post.downvotes.remove(request.user)
    else:
        post.downvotes.add(request.user)

    return redirect(request.META['HTTP_REFERER'])


def delete_comment(request, slug, comment_post):
    '''
    Function for deleting comments
    '''
    comment = get_object_or_404(Comment, pk=comment_post)
    comment.delete()

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def edit_comment(request, slug, comment_post):
    '''
    Function for editing user comments
    '''
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.get(pk=comment_post)
    comment_form = CommentForm(request.POST,
                               instance=comment)
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.post = post
            comment_form.save()
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm(instance=comment)
        return render(request, 'edit_comment.html', {'form': comment_form})


class PostList(ListView):
    '''
    Post list view which generates all posts and orderded by date
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        tag_menu = Tags.objects.all()
        tags = super(PostList, self).get_context_data(*args, **kwargs)
        tags["tag_menu"] = tag_menu
        return tags


class UserPostList(ListView):
    '''
    User posts view
    '''
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'user_posts.html'


class UserDraftList(ListView):
    '''
    Users drafts view
    '''
    model = Post
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'user_draft.html'


class EditDraft(UpdateView):
    '''
    Edit Draft view
    '''
    model = Post
    template_name = 'edit_draft.html'
    form_class = PostForm


class PostDetail(DetailView):
    '''
    Post view
    '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")

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

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment_form.instance.user = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )


class AddPost(CreateView):
    '''
    Add post view
    '''
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm

    # function which sets the author to be user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class EditPost(UpdateView):
    '''
    Edit post view
    '''
    model = Post
    template_name = 'edit_post.html'
    form_class = EditPostForm


class DeletePost(DeleteView):
    '''
    Delete post view
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def edit_profile(request, username):
    '''
    Edit profile function which calls two forms
    '''
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        edit_userprofile_form = EditUserProfileForm(request.POST,
                                                    request.FILES,
                                                    instance=profile)
        edit_user_form = EditUserForm(request.POST, instance=user)
        if edit_user_form.is_valid() and edit_userprofile_form.is_valid():
            edit_user_form.save()
            edit_userprofile_form.save()
            context = {
                'edit_userprofile_form': edit_userprofile_form,
                'edit_user_form': edit_user_form,
            }
            return render(request, 'account/edit_profile.html', context)
        else:
            context = {
                'edit_userprofile_form': edit_userprofile_form,
                'edit_user_form': edit_user_form,
            }
    else:
        edit_userprofile_form = EditUserProfileForm(instance=profile)
        edit_user_form = EditUserForm(instance=user)
        context = {
            'edit_userprofile_form': edit_userprofile_form,
            'edit_user_form': edit_user_form,
        }
        return render(request, 'account/edit_profile.html', context)


class ShowProfileView(DetailView):
    '''
    Show profile view which renders requested user profile
    '''
    model = User
    template_name = 'user_profile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))


def search_posts(request):
    '''
    Function which looks for posts with users requested words
    '''
    if request.method == "POST":
        searched = request.POST['searched']
        searched_posts = Post.objects.filter(title__contains=searched)
        return render(request, 'search_posts.html', {'searched': searched,
                      'searched_posts': searched_posts})
    else:
        return render(request, 'search_posts.html', {})
