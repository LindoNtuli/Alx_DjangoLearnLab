from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


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

# User Registration View
def register_view(request):
    return render(request, 'your_app/register.html') 
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to a home page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

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


