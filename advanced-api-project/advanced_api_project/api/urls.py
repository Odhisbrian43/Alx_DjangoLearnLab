from django.urls import path
from . import views

#url configuration for all views.
urlpatterns = [
    path('list/', views.BookListView, name = 'list'),
    path('book/', views.BookDetailView, name = 'book'),
    path('create/', views.BookCreateView, name='add-item'),
    path('update/<int:pk>/', views.BookUpdateView, name='update-book'),
    path('book/<int:pk>/delete/', views.BookDeleteView, name='delete-book')
]