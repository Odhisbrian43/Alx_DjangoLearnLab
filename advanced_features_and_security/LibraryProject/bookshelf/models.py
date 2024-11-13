from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission, Group

class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 100)
    publication_year = models.IntegerField()

    def __str__(self):
        return "f{self.title} {self.author} {self.publication_year}"
    
class CustomUser(AbstractUser):
        date_of_birth = models.DateField()
        profile_photo = models.ImageField()

class CustomUserManager(BaseUserManager):
       def create_user():
             return CustomUser
       def create_superuser():
             return CustomUser

class CustomUserAdmin(BaseUserManager):
      def ModelAdmin():
            create_useer = 'Add user'

can_view = Permission.objects.get(codename = 'can_view')

can_edit = Permission.objects.get(codename = 'can_edit')

can_create = Permission.objects.get(codename = 'can_create')

can_delete = Permission.objects.get(codename = 'can_delete')

Editors = Group.objects.create(name='Editors')

Editors.permissions.add(can_view, can_edit, can_create)

Viewers = Group.objects.create(name='Viewers')

Viewers.permissions.add(can_view)

Admins = Group.objects.create(name='Admins')

Admins.permissions.add(can_view, can_create, can_edit, can_delete)

