# api/serializers.py

from rest_framework import serializers
from .models import Book  # importing Book model

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
