from django.urls import path
from .views import register, user_login, user_logout
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register, name='register'),  # Registration view
    path('login/', user_login, name='login'),       # Login view
    path('logout/', user_logout, name='logout'),    # Logout view
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Include other URL patterns as required
]