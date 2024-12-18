#posts urls
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FeedViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedViewSet.as_view({'get': 'list'}), name='user_feed'),
    path('posts/', PostViewSet.as_view({'get': 'list'})),
    path('posts/<int:pk>/like/', PostViewSet.as_view({'post': 'like'})),
    path('posts/<int:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'})),
]
