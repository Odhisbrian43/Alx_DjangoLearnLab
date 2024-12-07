from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, Usercreationform, UserUpdateForm
from .models import Post, Comment
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate, login, logout, mixins
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .serializers import PostSerializer, CommentSerializer
from rest_framework import serializers, status,filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.
#views for the Post model.


class register(CreateView):
    form_class = Usercreationform
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #Redirect to a success page.
        ...
    else:
        #Redirect to an 'invalid credential' error page.
        ...

def logout_view(request):
    logout(request)
    #Redirects to a success message.

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

from django.shortcuts import render, get_object_or_404

# Create your views here.
#Generic views for deferent CRUD operations.
#This view retrieves all book instances
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostListView(request):
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'published_date']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'published_date']

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def PostDetailView(request):
    posts = Post.objects.all()
    post = request.query_params.get('id')
    #This checks confirms that the specific book exists then returns a view of the book.
    if post is not None:
        posts = posts.filter(specific_post = post)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #If the book does not exist the default return is of the book library.
    else:
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([LoginRequiredMixin])
def PostCreateView(request):

    post = PostSerializer(data=request.data)
 
    # validating for already existing data
    if Post.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if post.is_valid():
        post.save()
        return Response(post.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#View for updating a book view.
@api_view(['POST'])
@permission_classes([UserPassesTestMixin])
def PostUpdateView(request, pk):

    post = Post.objects.get(pk=pk)
    data = PostSerializer(instance=post, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([UserPassesTestMixin])
def PostDeleteView(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#Views for CRUD operations for comment model.
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CommentListView(request):
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['post', 'title', 'author', 'created_at']
    search_fields = ['title', 'author', 'post']
    ordering_fields = ['title', 'created_at']

    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def CommentDetailView(request):
    comments = Comment.objects.all()
    comment = request.query_params.get('id')
    #This checks confirms that the specific book exists then returns a view of the book.
    if comment is not None:
        comments = comments.filter(specific_comment = comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    #If the book does not exist the default return is of the book library.
    else:
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([LoginRequiredMixin])
def CommentCreateView(request):

    comment = CommentSerializer(data=request.data)
 
    # validating for already existing data
    # if Post.objects.filter(**request.data).exists():
    #     raise serializers.ValidationError('This data already exists')
 
    if comment.is_valid():
        comment.save()
        return Response(comment.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
#View for updating a book view.
@api_view(['POST'])
@permission_classes([UserPassesTestMixin])
def CommentUpdateView(request, pk):

    comment = Comment.objects.get(pk=pk)
    data = CommentSerializer(instance=comment, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@permission_classes([UserPassesTestMixin])
def CommentDeleteView(request, pk):

    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

#This view takes in a request and returns a list view of the query results.
class SearchResultsView(ListView):
    model = Post
    template_name = "search_results.html"

    def get_queryset(self): # new
        return Post.objects.filter(
            Q(name__icontains="") | Q(state__icontains="")
        )
    
#view for tag.
class TagView(CreateView):
    model = Tag
    template_name = 'serach.html'