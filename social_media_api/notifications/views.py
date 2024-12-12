from django.shortcuts import render
from .models import Notification
from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse_lazy
from accounts.forms import Usercreationform, ProfileUpdateForm, UserUpdateForm
from django.views.generic import CreateView, ListView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.permissions import IsAuthenticatedI
from django.http import Http404
from rest_framework import status
from accounts.serializers import FollowerSerializer

# Create your views here.
class LikeUnlikeView(APIView):
        permission_classes = [IsAuthenticatedI]
        
        def current_user(self):
            try:
                return User.objects.get(user = self.request.user)
            except User.DoesNotExist:
                raise Http404
            
        def other_user(self,pk):
            try:
                return User.objects.get(id = pk)
            except User.DoesNotExist:
                raise Http404
        
        def post(self, request,format=None): 
            "generics.get_object_or_404(Post, pk=pk)"   
            "Like.objects.get_or_create(user=request.user, post=post)",
            "Notification.objects.create"
            
            pk = request.data.get('id')              # Here pk is opposite user's profile ID
            req_type = request.data.get('type')        
            
            current_user = self.current_user()
            other_user = self.other_user(pk)
            
            
            if req_type == 'like_post':
                other_user.panding_request.add(current_user)
                return Response({"Requested" : "Follow request has been send!!"},status=status.HTTP_200_OK)
            
            elif req_type == 'accept':
                current_user.followers.add(other_user)
                other_user.following.add(current_user)
                current_user.panding_request.remove(other_user)
                return Response({"Accepted" : "Follow request successfuly accespted!!"},status=status.HTTP_200_OK)
            elif req_type == 'decline':
                current_user.panding_request.remove(other_user)
                return Response({"Decline" : "Follow request successfully declined!!"},status=status.HTTP_200_OK)
            elif req_type == 'unlike_post':
                current_user.following.remove(other_user)
                other_user.followers.remove(current_user)
                return Response({"Unlike" : "Unlike success!!"},status=status.HTTP_200_OK)
             # Here we can fetch followers,following detail and blocked user,pending request,sended request.. 
    
        def patch(self, request,format=None):
        
            req_type = request.data.get('type')
        
            if req_type == 'like_detail':
                serializer = FollowerSerializer(self.current_user())
                return Response({"data" : serializer.data},status=status.HTTP_200_OK)
