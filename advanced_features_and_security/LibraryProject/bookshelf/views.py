from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.
def Book_list(request):
    return render(request, 'bookshelf/index.html')

@permission_required
def raise_exception(request):
    if not request.create_user:
        return "you don't have the permission required"
    return render(request, 'book_list')