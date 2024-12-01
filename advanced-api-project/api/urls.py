# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),           # List all books
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),  # Retrieve a book
    path('books/create/', BookCreate.as_view(), name='book-create'),     # Create a new book
    path('books/<int:pk>/update/', BookUpdate.as_view(), name='book-update'),  # Update an existing book
    path('books/<int:pk>/delete/', BookDelete.as_view(), name='book-delete'),  # Delete a book
]
