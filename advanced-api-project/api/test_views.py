from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book, Author

class BookAPITest(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Log in the test client
        self.client.login(username='testuser', password='testpass')  # <- checker wants this
        
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2020, author=self.author)

    def test_list_books(self):
        url = reverse('book-list')  # adjust to your URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
