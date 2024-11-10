from django.urls import path
from .views import Book_list



urlpatterns = [
    path('', view = Book_list, name = "Book_list")
]