from django.contrib import admin
from .models import Author, Genre, Book, Borrow

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Borrow)

