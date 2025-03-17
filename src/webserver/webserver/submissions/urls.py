from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submissionsPage", views.submissionsPage, name="submissionsPage"),
    path('submissionsPage/<int:submission_id>/', views.submission_detail, name='submission'),
    path('downloadAllFiles/<int:submission_id>/', views.download_all_files, name='downloadAllFiles'),
]