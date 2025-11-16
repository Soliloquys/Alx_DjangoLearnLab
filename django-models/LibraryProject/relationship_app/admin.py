from django.contrib import admin

# Register your models here.
from .models import Library, Book, Librarian

admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Librarian)
