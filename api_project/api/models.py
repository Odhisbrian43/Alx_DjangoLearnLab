from django.db import models

# New model for the api app
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)