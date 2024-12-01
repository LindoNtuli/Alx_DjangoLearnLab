# api/views.py
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetch all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Fetch all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
