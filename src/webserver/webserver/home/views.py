from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request: HttpRequest):
    return render(request, 'home.html')

def homePage(request: HttpRequest):
    return render(request, 'homepage.html')