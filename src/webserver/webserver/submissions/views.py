from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Submission, SubmissionStatus
from .forms import FileUploadForm
from .tasks import run_submission
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def index(request: HttpRequest):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            submission: Submission = form.save(commit=False)
            submission.status = SubmissionStatus.objects.get(name="pending")
            submission.submitted_at = timezone.now()
            submission.save()

            # once submission is successfulled stored in db,
            # create a task to execute it

            run_submission(submission.id)
            return redirect('submissionsPage')
    else:
        form = FileUploadForm()
    return render(request, "submissions/index.html", {"form": form})

@login_required
def submissionsPage(request: HttpRequest):
    submissions = Submission.objects.all()

    return render(request, "submissions/submissions.html", {"submissions": submissions})