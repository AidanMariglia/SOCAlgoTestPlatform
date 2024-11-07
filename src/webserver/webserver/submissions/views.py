from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Submission, SubmissionStatus


def index(request: HttpRequest):
    if request.method == 'POST':
        status = SubmissionStatus.objects.get(name="pending")
        submitted_code = request.POST.get('submission')
        new_submission = Submission.objects.create(
            body=submitted_code,
            status=status
        )

        return redirect('submissionsPage')

def submissionsPage(request: HttpRequest):
    results = Submission.objects.all()

    return render(request, "submissions/index.html", {"results": results})