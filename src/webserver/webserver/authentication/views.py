from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request: HttpRequest):
    return render(request, 'home.html')

def register(request: HttpRequest):
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Create user and save to the database
        user = User.objects.create_user(username, email, password)
        
        # Update additional fields
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        user.save()

        messages.success(request, "Registration request successful. Please wait to be accepted!")
        return redirect('login')  # Redirect to the login page after successful registration

    return render(request, 'registration/register.html')