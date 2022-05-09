from .models import Post, Tags, UserProfile, Comment
from .forms import CommentForm, AddPostForm, EditUserProfileForm, EditUserForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
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


def DeleteComment(request, slug, comment_post):
    comment = get_object_or_404(Comment, pk=comment_post)
    comment.delete()

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def EditComment(request, slug, comment_post):
    post = get_object_or_404(Post, slug=slug)
    comment = Comment.objects.get(pk=comment_post)
    user = request.user
    comment_form = CommentForm(request.POST, instance=Comment.objects.get(pk=comment_post))
    if request.method == 'POST':
        if comment_form.is_valid():
            comment_form.instance.post = post
            comment_form.save()
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))
    else:
        comment_form = CommentForm(instance=Comment.objects.get(pk=comment_post))
        return render(request, 'edit_comment.html', {'form':comment_form})


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


class UserDraftList(ListView):
    model = Post
    queryset = Post.objects.filter(status=0).order_by('-created_on')
    template_name = 'user_draft.html'


class EditDraft(UpdateView):
    model = Post
    template_name = 'edit_draft.html'
    fields = ['title', 'content', 'status']


class PostDetail(DetailView):

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
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
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


# class EditProfileView(UpdateView):
#     form_class = EditProfileForm
#     template_name = 'account/edit_profile.html'
#     success_url = reverse_lazy('home')

#     def get_object(self):
#         return self.request.user


# def EditProfile(request, username):
#     user = request.user
#     profile = get_object_or_404(UserProfile, user=user)
#     if request.method == 'POST':
#         edit_profile_form = EditProfileForm(request.POST, request.FILES, instance=profile,
#         initial={'first_name':user.first_name,'last_name':user.last_name})
#         if edit_profile_form.is_valid():
#             print(edit_profile_form)
#             # new_form = edit_profile_form.save(commit=False)
#             # new_form.user_bio = request.POST.get('user_bio')
#             # new_form.save()
#             edit_profile_form.save()
#             return render(request, 'account/edit_profile.html', {'form':edit_profile_form})
#         else:
#             return render(request, 'account/edit_profile.html', {'form':edit_profile_form})
#     else:
#         edit_profile_form = EditProfileForm(instance=profile,initial={'first_name':user.first_name, 
#                                                                         'last_name':user.last_name})
#         return render(request, 'account/edit_profile.html', {'form':edit_profile_form})


def EditProfile(request, username):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        edit_userprofile_form = EditUserProfileForm(request.POST, request.FILES, instance=profile)
        edit_user_form = EditUserForm(request.POST, instance=user)
        if edit_user_form.is_valid() and edit_userprofile_form.is_valid():
            edit_user_form.save()
            edit_userprofile_form.save()
            edit_userprofile_form = EditUserProfileForm(instance=profile)
            edit_user_form = EditUserForm(instance=user)
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


def SearchPosts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        searched_posts = Post.objects.filter(title__contains=searched)
        return render(request, 'search_posts.html',{'searched': searched, 'searched_posts': searched_posts})
    else:
        return render(request, 'search_posts.html',{})