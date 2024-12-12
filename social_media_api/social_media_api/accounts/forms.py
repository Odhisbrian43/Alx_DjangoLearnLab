from django.contrib.auth import models, forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#Form for new user registration.
class Usercreationform(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def save(self, commit=True):
        user = super(Usercreationform, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

#Profile update form.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = models.User
        fields = ['username', 'email']