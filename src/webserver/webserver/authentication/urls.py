from django.urls import path

from . import views
from . import admin

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register, name='register'),
    path("users", admin.users, name='users'),
]