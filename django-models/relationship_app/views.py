from django.shortcuts import render
from .models import Book 
from django.views.generic import DetailView
from relationship_app.models import Library
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.

def list_books(request):

    books = Book.objects.all()

    context = {'book_lists', books}

    return render(request, "relationship_app/lists_books.html", context)


class Books(DetailView):

    model = Library

    template_name = 'relationship_app/library_detail.html'

    def all_books(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context = self.get_object()

        return context
    
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        ...
    else:
        ...

def logout_view(request):
    logout(request)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'