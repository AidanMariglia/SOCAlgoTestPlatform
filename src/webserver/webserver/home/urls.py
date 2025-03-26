from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("help/", views.help, name="help"),
    path("help/valid-files/", views.valid_files, name="valid_files"),
    path("help/code-ownership/", views.ownership, name="code_ownership"),
]