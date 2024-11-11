import subprocess
import os

from django.utils import timezone
from workers import task
from .models import Submission, SubmissionStatus


@task()
def run_submission(submission_id):
    print(f"Running submission {submission_id}")
    
    s: Submission = Submission.objects.get(id=submission_id)
    file_path = s.file.path

    # doesn't work if you start workers from vscode, need to start workers form terminal
    result = subprocess.run(['octave', str(file_path)], capture_output=True, text=True)

    s.result = result.stdout
    s.status = SubmissionStatus.objects.get(name="completed")
    s.completed_at = timezone.now()

    s.save()
    