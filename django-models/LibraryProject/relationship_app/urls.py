from django.urls import path
from . import views
from .views import register, user_login, user_logout
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('books/add/', add_book, name='add_book'),
    path('books/edit/<int:book_id>/', edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete_book'),
    
]

