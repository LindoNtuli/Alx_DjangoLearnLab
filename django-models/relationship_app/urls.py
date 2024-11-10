from django.urls import path
from .views import list_books, LibraryDetailView
from .views import register, user_login, user_logout
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('register/', register, name='register'),  # Link to the registration view
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # User login
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # User logout
]

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path, include

urlpatterns = [
    path('relationship/', include('relationship_app.urls')),
    # other URL patterns...
]
