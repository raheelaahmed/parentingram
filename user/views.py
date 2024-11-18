from django.shortcuts import render
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.

def profile(request):
    return render(request, "profile.html")