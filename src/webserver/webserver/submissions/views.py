from django.http import HttpRequest
from django.shortcuts import render, redirect
from .models import Submission, SubmissionStatus
from .forms import FileUploadForm
from .tasks import run_submission
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404

@login_required
def index(request: HttpRequest):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            submission: Submission = form.save(commit=False)
            submission.status = SubmissionStatus.objects.get(name="pending")
            submission.submitted_at = timezone.now()
            submission.user = request.user
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
    submissions = Submission.objects.all().filter(user=request.user)

    return render(request, "submissions/submissions.html", {"submissions": submissions})

@login_required
def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    # Check if the logged-in user is the owner of the submission
    if submission.user != request.user:
        raise Http404("You are not authorized to view this submission.")

    return render(request, 'submissions/submission.html', {'submission': submission})