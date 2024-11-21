from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('Book/', BookList.as_view(), name='book_list'), #map to the book list view

    #all urls for BookViewSet's all CRUD operations
    path('', include(router.urls)),

    #apie view authentication for username and password
    path('api-token-auth/', views.obtain_auth_token)
]