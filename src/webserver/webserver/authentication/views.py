from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from authentication.models import CustomUser

User = get_user_model()

def register(request: HttpRequest):
    if request.method == 'POST':
        # Get form data from the POST request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        academic_affiliation = request.POST.get('academic_affiliation', '')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        # Create user and save to the database
        user = CustomUser.objects.create_user(username, email, password)
        
        # Update additional fields
        user.first_name = first_name
        user.last_name = last_name
        user.academic_affiliation = academic_affiliation
        user.save()

        messages.success(request, "Registration successful!")
        return redirect('/home')  # Redirect to the home page after successful registration

    return render(request, 'registration/register.html')