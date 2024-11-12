from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta(models.Model):
        permissions = (
            can_add_book
            can_change_book
            can_delete_book
        )

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, primary_key=True)

user = User.objects.create_user('john', 'john@example.com', 'password123')

user = User.objects.get(username='john')

class UserProfile(models.Model):
    "Admin",
    "Member"
    user = models.OneToOneField(User)

    class Roles(models.TextChoices):
        ADMIN = "a", _("Admin")
        LIBRARIAN = "l", _("Librarian")
        MEMBER = "m", _("Member")

    role = models.CharField(
        max_length=1,
        choices = role_choices
    )
    