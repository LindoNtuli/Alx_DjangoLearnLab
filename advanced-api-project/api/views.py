# api/views.py
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    This includes list, create, retrieve, update, and delete operations.
    """
    queryset = Book.objects.all()  # Get all books
    serializer_class = BookSerializer  # Use the defined serializer for the Book model

# List and Create Authors
class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Retrieve, Update, and Delete Author
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# List and Create Books
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, Update, and Delete Book
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
