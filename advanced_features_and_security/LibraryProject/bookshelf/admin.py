from django.contrib import admin
from .models import Book

# Register your models here.

admin.ModelAdmin

admin.site.register(Book)

"list_filter", "author", "publication_year"

"search_fields", "title"