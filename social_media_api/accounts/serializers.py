from rest_framework import serializers
from .models import User

#serializers for models.

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class FollowerSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True, read_only= True)
    following = UserSerializer(many=True,read_only=True)
    
    class Meta:
        model = User
        fields = ('followers','following')
        read_only_fields = ('followers','following')