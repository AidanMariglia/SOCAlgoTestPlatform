from django.http import HttpRequest
from django.shortcuts import render
from django.db.models.functions import Length

from submissions.models import Submission

# Create your views here.

def leaderboard(request: HttpRequest):
    results = Submission.objects.all().exclude(result="").order_by(Length("result").desc())

    return render(request, "leaderboard/leaderboard.html", {"results": results})