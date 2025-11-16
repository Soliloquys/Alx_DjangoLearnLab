from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949) 
>>> book
<Book: Book object (1)>

books = Book.objects.all()
>>> books
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

book.title = "Nineteen Eighty-Four"
book.save()
book
<Book: Nineteen Eighty-Four>

book.delete()
Book.objects.all()
empty queryset QuerySet []