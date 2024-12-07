from django.urls import path
from . import views

#url paths for the wies created.

urlpatterns = [
    path('login/', view=views.login_view,name=('login')),
    path('logout/', view=views.logout_view, name=('logout')),
    path('register/', views.register.as_view, name=('register')),
    path('profile/', view=views.profile, name=('profile')),
    path('posts/', view=views.PostListView, name=('posts')),
    path('post/new/', view=views.PostCreateView, name=('new post')),
    path('post/<int:pk>/', view=views.PostDetailView, name=('details')),
    path('post/<int:pk>/update/', view=views.PostUpdateView, name=('post editing')),
    path('post/<int:pk>/delete/', view=views.PostDeleteView, name=('post delete')),
    path('post/<int:post_id>/comments/new/', view=views.CommentCreateView, name=('new comment')),
    path('post/<int:post_id>/comments/list/', view=views.CommentListView, name=('all comments')),
    path('post/<int:post_id>/comments/<int:pk>/update/', view=views.CommentUpdateView, name=('edit comment')),
    path('post/<int:post_id>/comments/<int:pk>/', view=views.CommentDetailView),
    path('post/<int:post_id>/comments/<int:pk>/delete/', view=views.CommentDeleteView, name=('delete comment')),
    path('post/tags/<tag_name>/', view=views.TagView.as_view, name=('Tag view')),
    path('post/search/', view=views.SearchResultsView.as_view, name=('serach result')),
]