from django.db import models
from accounts.models import User

# Create your models here.
#Model for posts.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField

    def __str__(self):
        return f"Post by {self.author}, {self.title}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField

class Like(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




