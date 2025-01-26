from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.admin.views.decorators import staff_member_required

User = get_user_model()

@staff_member_required()
def users(request: HttpRequest):
    if request.method == 'POST':

        username = request.POST['username']

        # Activate user
        user = User.objects.get(username=username)

        user.is_active = True

        user.save()

    # Lists all users that aren't admins
    users = User.objects.filter(is_staff=False)

    return render(request, 'registration/users.html', {"users": users})