from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic.detail import DetailView   # REQUIRED BY ALX

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# Class-based view: library detail
class LibraryDetailView(DetailView):   # REQUIRED BY ALX
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
