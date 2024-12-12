from rest_framework import routers
from django.urls import path
from . import views
from notifications.views import LikeUnlikeView

#Creating routers for for Crud operation views.

router = routers.SimpleRouter()
router.register(r'posts/', views.PostViewSet, basename='post')
router.register(r'comments/', views.CommentViewSet, basename='comments')
router.register(r'feed/', views.PostViewSet, basename='feed')
urlpatterns = [
    router.urls,
    path('/posts/<int:pk>/like/', view=LikeUnlikeView, name='post likes'),
    path('/posts/<int:pk>/unlike/', view=LikeUnlikeView, name='post unlike'),
    ]