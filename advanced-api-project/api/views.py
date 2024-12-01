from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, serializers, status,filters
from .models import Book, Author
from .serializers import BookSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
#Generic views for deferent CRUD operations.
#This view retrieves all book instances
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def BookListView(request):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']

    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def BookDetailView(request):
    books = Book.objects.all()
    book = request.query_params.get('id')
    #This checks confirms that the specific book exists then returns a view of the book.
    if book is not None:
        books = books.filter(specific_book = book)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #If the book does not exist the default return is of the book library.
    else:
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BookCreateView(request):

    book = BookSerializer(data=request.data)
 
    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if book.is_valid():
        book.save()
        return Response(book.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#View for updating a book view.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BookUpdateView(request, pk):

    book = Book.objects.get(pk=pk)
    data = BookSerializer(instance=book, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def BookDeleteView(request, pk):

    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


# class BookCreatView(viewsets.ModelViewSet):
#     #This generic view creates a new Book instance.
#     queryset = 
#     serializer_class = BookSerializer