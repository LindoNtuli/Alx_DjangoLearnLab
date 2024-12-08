from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import post_detail, edit_comment, delete_comment
from .views import CommentCreateView, CommentUpdateView, CommentDeleteView
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('comment/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/edit/<pk>/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/delete/<pk>/', CommentDeleteView.as_view(), name='comment_delete'),
]
