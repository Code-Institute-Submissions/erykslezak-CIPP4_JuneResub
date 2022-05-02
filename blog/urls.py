from . import views
from django.urls import path
from .views import AddPost, PostDetail, EditPost

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('edit_post/<int:pk>', EditPost.as_view(), name="edit_post"),
    path('<slug:slug>/', PostDetail.as_view(), name="post_detail"),
]