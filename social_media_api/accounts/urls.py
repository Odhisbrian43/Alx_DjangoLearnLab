from django.urls import path
from .views import Register, LoginView, profile, FollowUnfollowView

#Url for register and log in view.

urlpatterns = [
    path('login/', view=LoginView.as_view(), name='login'),
    path('register/', view=Register.as_view(), name='register'),
    path('profile/', view=profile, name="profile"),
    path('profile/follow/<int:user_id>/', view=FollowUnfollowView.as_view(), name='follow'),
    path('profile/follow/<int:user_id>/', view=FollowUnfollowView.as_view, name='unfollow'),

]