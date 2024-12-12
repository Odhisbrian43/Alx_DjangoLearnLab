from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy
from django.conf import settings
from datetime import date

#A user creation that is an extention of Abstractuser with extended fields.
class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, blank=True)
    email = models.EmailField(('email address'), unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField
    followers = models.ManyToManyField("self", related_name='users_followers', symmetrical=False)
    followings = models.ManyToManyField("self", related_name='user_interests', symmetrical=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    #format the the lable to a string username.
    def __str__(self):
        return f"{self.username}"