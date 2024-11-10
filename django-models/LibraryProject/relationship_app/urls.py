from django.urls import path
from .views import list_books
from .views import Books

urlpatterns = [
    path('', view=list_books, name='Books_list'),
    path('', Books.as_view(), name='Books')
]