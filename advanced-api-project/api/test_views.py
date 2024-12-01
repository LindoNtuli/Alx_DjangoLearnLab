# api/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.book_data = {'title': 'Test Book', 'author': 'Author Name', 'publication_year': 2023}

    def test_create_book(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('book-create'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_get_book_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        self.client.login(username='testuser', password='testpassword')
        book = Book.objects.create(**self.book_data)
        update_data = {'title': 'Updated Book'}
        response = self.client.put(reverse('book-update', kwargs={'pk': book.id}), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, 'Updated Book')

    def test_delete_book(self):
        self.client.login(username='testuser', password='testpassword')
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(reverse('book-delete', kwargs={'pk': book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_unauthenticated_user_cannot_create_book(self):
        response = self.client.post(reverse('book-create'), self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authentication_required(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

