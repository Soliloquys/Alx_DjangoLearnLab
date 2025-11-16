from .models import Library, Book

# Get all books
all_books = Book.objects.all()

# Get all libraries
all_libraries = Library.objects.all()

# Filter books by publication year
books_2020 = Book.objects.filter(publication_year=2020)

# Get a specific library and its books
library = Library.objects.get(id=1)
library_books = library.books.all()
