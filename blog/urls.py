'''
Imports the relevant packages
'''
from django.urls import path
from . import views
from .views import (AddPost, PostDetail, EditPost, DeletePost, UserPostList,
                    tags_view, upvote_view, downvote_view, edit_profile,
                    delete_comment, edit_comment, UserDraftList,
                    EditDraft, search_posts, ShowProfileView)

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('user-posts/<str:username>', UserPostList.as_view(),
         name='user_posts'),
    path('user-draft/<str:username>', UserDraftList.as_view(),
         name='user_drafts'),
    path('edit-draft/<slug:slug>', EditDraft.as_view(), name="edit_draft"),
    path('account/edit-profile/<str:username>', edit_profile,
         name="edit_profile"),
    path('users/<str:username>', ShowProfileView.as_view(),
         name="show_profile"),
    path('add-post/', AddPost.as_view(), name="add_post"),
    path('edit-post/<slug:slug>', EditPost.as_view(), name="edit_post"),
    path('delete-post/<slug:slug>', DeletePost.as_view(), name="delete_post"),
    path('<slug:slug>/<int:comment_post>/delete', delete_comment,
         name='delete_comment'),
    path('<slug:slug>/<int:comment_post>/edit', edit_comment,
         name='edit_comment'),
    path('tags/<str:tags>/', tags_view, name="tags"),
    path('search_posts/', search_posts, name="search_posts"),
    path('upvote/<slug:slug>', upvote_view, name='upvote_post'),
    path('downvote/<slug:slug>', downvote_view, name='downvote_post'),
    path('<slug:slug>/', PostDetail.as_view(), name="post_detail"),
]
