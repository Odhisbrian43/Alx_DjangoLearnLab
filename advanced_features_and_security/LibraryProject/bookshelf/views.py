from django.shortcuts import render

# Create your views here.
def Book_list(request):
    return render(request, 'bookshelf/index.html')
