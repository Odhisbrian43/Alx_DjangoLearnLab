from django.contrib import admin
from .models import Book, CustomUser, CustomUserAdmin

# Register your models here.

admin.ModelAdmin

admin.site.register(Book)

"list_filter", "author", "publication_year"

"search_fields", "title"

admin.site.register(CustomUser, CustomUserAdmin)