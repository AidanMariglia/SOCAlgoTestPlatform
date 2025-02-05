from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request: HttpRequest):
    user = request.user
    return render(request, 'home.html', {"user": user})

def homePage(request: HttpRequest):
    return render(request, 'intro.html')