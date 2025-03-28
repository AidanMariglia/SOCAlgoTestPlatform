from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

User = get_user_model()

def home(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home.html', {"user": user})
    else:
        return render(request, 'intro.html')
    
def help(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-help.html', {"user": user})
    else:
        return render(request, 'intro-help.html')
    
def valid_files(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-valid_files.html', {"user": user})
    else:
        return render(request, 'intro-valid_files.html')
    
def ownership(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-ownership.html', {"user": user})
    else:
        return render(request, 'intro-ownership.html')
    
def private(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-private-submission.html', {"user": user})
    else:
        return render(request, 'intro-private-submission.html')
    
def sub_process(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-sub-process.html', {"user": user})
    else:
        return render(request, 'intro-sub-process.html')
    
def verification(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-verification.html', {"user": user})
    else:
        return render(request, 'intro-verification.html')
    
def forgot_password(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-forgot-password.html', {"user": user})
    else:
        return render(request, 'intro-forgot-password.html')
    
def forgot_username(request: HttpRequest):
    user = request.user

    if request.user.is_authenticated:
        return render(request, 'home-forgot-username.html', {"user": user})
    else:
        return render(request, 'intro-forgot-username.html')
    
def logout_view(request):
    logout(request)
    return render(request, 'intro.html')