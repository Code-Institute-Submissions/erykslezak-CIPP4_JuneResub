from . import views
from django.urls import path
from .views import AddPost, PostDetail, EditPost, DeletePost, UserPostList, TagsView, UpvoteView, DownvoteView, UpvoteViewIndex, DownvoteViewIndex, EditProfile, DeleteComment, EditComment, UserDraftList, EditDraft, SearchPosts

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user-posts/<str:username>', views.UserPostList.as_view(), name='user_posts'),
    path('user-draft/<str:username>', views.UserDraftList.as_view(), name='user_drafts'),
    path('edit-draft/<slug:slug>', EditDraft.as_view(), name="edit_draft"),
    path('account/edit-profile/<str:username>', EditProfile, name="edit_profile"),
    path('add-post/', AddPost.as_view(), name="add_post"),
    path('edit-post/<slug:slug>', EditPost.as_view(), name="edit_post"),
    path('delete-post/<slug:slug>', DeletePost.as_view(), name="delete_post"),
    path('<slug:slug>/<int:comment_post>/delete', DeleteComment, name='delete_comment'),
    path('<slug:slug>/<int:comment_post>/edit', EditComment, name='edit_comment'),
    path('tags/<str:tags>/', TagsView, name="tags"),
    path('search_posts', views.SearchPosts, name="search_posts"),
    path('upvote/<slug:slug>', UpvoteView, name='upvote_post'),
    path('downvote/<slug:slug>', DownvoteView, name='downvote_post'),
    path('upvote_index/', UpvoteViewIndex, name='upvote_post_index'),
    path('downvote_index/', DownvoteViewIndex, name='downvote_post_index'),
    path('<slug:slug>/', PostDetail.as_view(), name="post_detail"),
]