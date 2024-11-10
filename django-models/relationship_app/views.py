from django.shortcuts import render, redirect
from django.contrib.auth.forms import register
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Library, Book
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('home')  # Redirect to home or another page after registration
    else:
        form = register()  # Show the empty form

    return render(request, 'relationship_app/register.html', {'form': form})
# User Registration View

# User Login View
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page after logging in
        else:
            return render(request, 'relationship_app/login.html', {'error': 'Invalid username or password'})
    return render(request, 'relationship_app/login.html')

# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Specify the template path
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Add books associated with the library
        return context
