from django.shortcuts import render, redirect
from .models import User
from django.urls import reverse_lazy
from .forms import Usercreationform, ProfileUpdateForm, UserUpdateForm
from django.views.generic import CreateView, ListView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
#User registration view.

class Register(CreateView):
    form_class = Usercreationform
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

class LoginView(APIView):
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
