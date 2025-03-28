from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("help/", views.help, name="help"),
    path("help/valid-files/", views.valid_files, name="valid_files"),
    path("help/code-ownership/", views.ownership, name="code_ownership"),
    path("help/submission-process/", views.private, name="code_ownership"),
    path("help/public-private-submission/", views.sub_process, name="code_ownership"),
    path("help/account-verification/", views.verification, name="code_ownership"),
    path("help/forgot-username/", views.forgot_username, name="code_ownership"),
    path("help/forgot-password/", views.forgot_password, name="code_ownership"),
]