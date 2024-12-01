# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import AuthorListCreate, AuthorDetail, BookListCreate, BookDetail

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]
