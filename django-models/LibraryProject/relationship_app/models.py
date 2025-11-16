from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username
