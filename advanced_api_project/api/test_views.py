from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name="Author 1")
        self.book = Book.objects.create(title="Book 1", publication_year=2025, author=self.author)

    def test_list_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        response = self.client.post('/api/books/create/', {'title':'Book 2','publication_year':2024,'author':self.author.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
