from django.shortcuts import render
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import serializers, filters, status, response, viewsets, permissions
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404

# Create your views here.
#views for comment CRUD operations.

class CommentViewSet(viewsets.ModelViewSet):

    @api_view(['GET'])
    @permission_classes([IsAuthenticatedOrReadOnly])
    def CommentListView(request):
        filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = ['post', 'title', 'author', 'created_at']
        search_fields = ['title', 'author', 'post']
        ordering_fields = ['title', 'created_at']

        comments = Comment.objects.all()
        paginator = paginator(comments, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        #serializer = PostSerializer(posts, many=True)
        return render(request, "posts/comment_list.html", {"page_obj": page_obj})
        #serializer = CommentSerializer(comments, many=True)
        #return response.Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    @permission_classes([IsAuthenticatedOrReadOnly])
    def CommentDetailView(request):
        comments = Comment.objects.all()
        comment = request.query_params.get('id')
        #This checks confirms that the specific book exists then returns a view of the book.
        if comment is not None:
            comments = comments.filter(specific_comment = comment)
            serializer = CommentSerializer(comments, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        #If the book does not exist the default return is of the book library.
        else:
            serializer = CommentSerializer(comments, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['POST'])
    @permission_classes([LoginRequiredMixin])
    def CommentCreateView(request):

        comment = CommentSerializer(data=request.data)
    
        # validating for already existing data
        # if Post.objects.filter(**request.data).exists():
        #     raise serializers.ValidationError('This data already exists')
    
        if comment.is_valid():
            comment.save()
            return response.Response(comment.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        
    #View for updating a book view.
    @api_view(['POST'])
    @permission_classes([UserPassesTestMixin])
    def CommentUpdateView(request, pk):

        comment = Comment.objects.get(pk=pk)
        data = CommentSerializer(instance=comment, data=request.data)
    
        if data.is_valid():
            data.save()
            return response.Response(data.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)


    @api_view(['DELETE'])
    @permission_classes([UserPassesTestMixin])
    def CommentDeleteView(request, pk):

        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return response.Response(status=status.HTTP_202_ACCEPTED)

#views for post CRUD operations.

class PostViewSet(viewsets.ViewSet):

    @api_view(['GET'])
    @permission_classes([IsAuthenticatedOrReadOnly])
    def PostListView(request):
        filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
        filterset_fields = ['title', 'author', 'published_date']
        search_fields = ['title', 'author']
        ordering_fields = ['title', 'published_date']

        posts = Post.objects.all()
        paginator = paginator(posts, 20)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        #serializer = PostSerializer(posts, many=True)
        return render(request, "posts/post_list.html", {"page_obj": page_obj})
        #return response.Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['GET'])
    @permission_classes([IsAuthenticatedOrReadOnly])
    def PostDetailView(request):
        #posts = Post.objects.all()
        post = request.query_params.get('id')
        #This checks confirms that the specific book exists then returns a view of the book.
        if post is not None:
            posts = Post.objects.filter(author__in=following_users).order_by
            serializer = PostSerializer(posts, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        #If the book does not exist the default return is of the book library.
        else:
            serializer = PostSerializer(posts, many=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(['POST'])
    @permission_classes([permissions.IsAuthenticated])
    def PostCreateView(request):

        post = PostSerializer(data=request.data)
    
        # validating for already existing data
        if Post.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already exists')
    
        if post.is_valid():
            post.save()
            return response.Response(post.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        
    #View for updating a book view.
    @api_view(['POST'])
    @permission_classes([UserPassesTestMixin])
    def PostUpdateView(request, pk):

        post = Post.objects.get(pk=pk)
        data = PostSerializer(instance=post, data=request.data)
    
        if data.is_valid():
            data.save()
            return response.Response(data.data)
        else:
            return response.Response(status=status.HTTP_404_NOT_FOUND)


    @api_view(['DELETE'])
    @permission_classes([UserPassesTestMixin])
    def PostDeleteView(request, pk):

        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return response.Response(status=status.HTTP_202_ACCEPTED)
    
    @api_view(['GET'])
    @permission_classes([LoginRequiredMixin])
    def feedsview(request, page):
         # Pull the data
        object_list = Post.objects.all()
    
    # Pull the proper items for this page
        paginator = Paginator(object_list, 100)
        try:
            page_obj = paginator.page(page)
        except InvalidPage:
        # Return 404 if the page doesn't exist
            raise Http404
    
    # Pass out the data
        context = {
        "object_list": page_obj.object_list,
        "page": page_obj,
        }
        template = 'newtwitter_pagination/tracks.json'
        return render(request, template, context, 'text/javascript')
