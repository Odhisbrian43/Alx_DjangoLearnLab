from django.urls import path
from . import views

#url configuration for all views.
urlpatterns = [
    path('list/', views.BookListView, name = 'list'),
    path('books/', views.BookDetailView, name = 'book'),
    path('books/create/', views.BookCreateView, name='add-item'),
    path('books/update/<int:pk>/', views.BookUpdateView, name='update-book'),
    path('books/delete/<int:pk>/delete/', views.BookDeleteView, name='delete-book')
]