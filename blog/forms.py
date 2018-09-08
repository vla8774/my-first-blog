from django_comments import forms
from requests import auth

from .models import Profile

class UserEditForm(forms.ModelForm):
    class Meta:
        model = auth.User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = 'photo'
