from django.contrib.auth import models, forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django import forms
from taggit.managers import TaggableManager

#creating a custom user creation form that includes extra fields.

class Usercreationform(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = models.User
        fields = ("username", "email", "password", "password2")

    def save(self, commit=True):
        user = super(Usercreationform, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
# Create a UserUpdateForm to update a username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = models.User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image.
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

#Comment form with creation and updating of comments.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

#Post creation and update form.
class PostForm:
    class Meta:
        model = Post
        fields = '__all__'

class TagWidget():
    def __init__(self, attrs=None):
        days = {day: day for day in range(1, 32)}
        months = {month: month for month in range(1, 13)}
        years = {year: year for year in [2018, 2019, 2020]}
        widgets = [
            forms.Select(attrs=attrs, choices=days),
            forms.Select(attrs=attrs, choices=months),
            forms.Select(attrs=attrs, choices=years),
        ]
        super().__init__(widgets, attrs)

    def tag(request, ):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
        # Without this next line the tags won't be saved.
                form.save_m2m()