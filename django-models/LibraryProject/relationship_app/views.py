from django.shortcuts import render, get_object_or_404
from .models import Library, Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def library_detail(request, library_id):
    library = get_object_or_404(Library, id=library_id)
    books = library.books.all()
    return render(request, 'relationship_app/library_detail.html', {'library': library, 'books': books})
