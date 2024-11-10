from django.urls import path
from .views import register  # Import the register view

urlpatterns = [
    path('register/', register, name='register'),  # Link to the registration view
]
from .views import user_login, user_logout
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('login/', user_login, name='login'),       # Login view
    path('logout/', user_logout, name='logout'),    # Logout view
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Include other URL patterns as required
]

