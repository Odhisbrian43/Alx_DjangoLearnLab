from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse_lazy
from .forms import Usercreationform, ProfileUpdateForm, UserUpdateForm
from django.views.generic import CreateView, ListView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.permissions import IsAuthenticatedI
from django.http import Http404
from rest_framework import status
from .serializers import FollowerSerializer

# Create your views here.
#User registration view.

class Register(CreateView):
    form_class = Usercreationform
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

class LoginView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        #user authentication.
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

class FollowUnfollowView(generics.GenericAPIView):
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
            
            pk = request.data.get('id')              # Here pk is opposite user's profile ID
            req_type = request.data.get('type')        
            
            current_user = self.current_user()
            other_user = self.other_user(pk)
            
            
            if req_type == 'follow_user':
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
            elif req_type == 'unfollow_user':
                current_user.following.remove(other_user)
                other_user.followers.remove(current_user)
                return Response({"Unfollow" : "Unfollow success!!"},status=status.HTTP_200_OK)
             # Here we can fetch followers,following detail and blocked user,pending request,sended request.. 
    
        def patch(self, request,format=None):
        
            req_type = request.data.get('type')
        
            if req_type == 'follow_detail':
                serializer = FollowerSerializer(self.current_user())
                return Response({"data" : serializer.data},status=status.HTTP_200_OK)
