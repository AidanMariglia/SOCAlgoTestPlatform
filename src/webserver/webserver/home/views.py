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
    
def logout_view(request):
    logout(request)
    return render(request, 'intro.html')