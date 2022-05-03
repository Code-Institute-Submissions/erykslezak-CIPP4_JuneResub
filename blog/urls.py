from . import views
from django.urls import path
from .views import AddPost, PostDetail, EditPost, DeletePost, UserPostList, TagsView, UpvoteView, DownvoteView, UpvoteViewIndex, DownvoteViewIndex, EditProfileView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user_posts/<str:username>', views.UserPostList.as_view(), name='user_posts'),
    path('account/edit_profile', EditProfileView.as_view(), name="edit_profile"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('edit_post/<slug:slug>', EditPost.as_view(), name="edit_post"),
    path('delete_post/<slug:slug>', DeletePost.as_view(), name="delete_post"),
    path('tags/<str:tags>/', TagsView, name="tags"),
    path('upvote/<slug:slug>', UpvoteView, name='upvote_post'),
    path('downvote/<slug:slug>', DownvoteView, name='downvote_post'),
    path('upvote_index/', UpvoteViewIndex, name='upvote_post_index'),
    path('downvote_index/', DownvoteViewIndex, name='downvote_post_index'),
    path('<slug:slug>/', PostDetail.as_view(), name="post_detail"),
]