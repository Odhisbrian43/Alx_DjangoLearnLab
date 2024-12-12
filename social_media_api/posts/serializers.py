from .models import Post, Comment
from rest_framework import serializers
#Serializers for posts models.

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    class Meta:
        model = Comment
        fields = '__all__'