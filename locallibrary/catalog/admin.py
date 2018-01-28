from django.contrib import admin

# Register your models here.
from .models import Author, Book, Genre, BookInstance, Language

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(BookInstance)
admin.site.register(Language)