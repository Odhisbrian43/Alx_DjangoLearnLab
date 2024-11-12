from django.urls import path
from .views import list_books
from .views import Books
LibraryDetailView"

urlpatterns = [
    path('', view=list_books, name='Books_list'),
    path('', Books.as_view(), name='Books')
    path('', view = views.register, name = 'register')
    path('', LogoutView.as_view(template_name="logout"))
    path('', LoginView.as_view(template_name='login'))
    path('add_book/',)
    path('edit_book/',)
    path('delete_book', )
]