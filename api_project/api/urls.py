# api/urls.py

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Import the token view
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import BookList

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),  # This includes all routes registered with the router
]
