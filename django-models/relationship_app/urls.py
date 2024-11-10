from django.urls import path
from .views import register  # Import the register view
from .views import admin_view, librarian_view, member_view

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
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    # Include other URL patterns as required
]

