from django import forms
from .models import Book  # Make sure to import your Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'isbn']  # Adjust fields as necessary
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
