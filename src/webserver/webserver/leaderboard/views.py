from django.http import HttpRequest
from django.shortcuts import render
from django.db.models.functions import Length

from submissions.models import Submission

# Create your views here.

def leaderboard(request: HttpRequest):

    order_by = request.GET.get('order_by', "weighted_error")

    submissions = Submission.objects.filter(status__name="completed").order_by(order_by)
    return render(request, "leaderboard/leaderboard.html", {"submissions": submissions})