from django import forms
from .models import Profile





#update profile
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','username','email']

