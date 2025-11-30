from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Author, Book

class BookAPITest(APITestCase):
    def setUp(self):
        # create sample author and book
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2025, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')  # adjust if your URL name is different
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
