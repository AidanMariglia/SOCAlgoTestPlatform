from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Submission, SubmissionStatus
from .forms import FileUploadForm
from django.utils import timezone

def index(request: HttpRequest):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.status = SubmissionStatus.objects.get(name="pending")
            submission.submitted_at = timezone.now()
            submission.save()
            return redirect('submissionsPage')
    else:
        form = FileUploadForm()
    return render(request, "submissions/index.html", {"form": form})

def submissionsPage(request: HttpRequest):
    submissions = Submission.objects.all()

    return render(request, "submissions/submissions.html", {"submissions": submissions})