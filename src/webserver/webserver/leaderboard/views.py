from django.http import HttpRequest
from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Exists, OuterRef

from submissions.models import Submission
from django.contrib.auth import get_user_model


Users = get_user_model()
# Create your views here.

MODEL_TYPE_MAP={
    "Machine Learning": "ML",
    "Kalman Fitler":    "KF",
    "Not Specified":    "NA"
}
MODEL_TYPE_CHOICES=["Machine Learning", "Kalman Fitler", "Not Specified"]

def leaderboard(request: HttpRequest):

    user_id = request.GET.get('author')
    mt = request.GET.get('modeltype')

    order_by = request.GET.get('order_by', "weighted_error")

    # get all users with at least 1 submission
    users = Users.objects.filter(Exists(Submission.objects.filter(user=OuterRef("id"))))

    submissions = Submission.objects.filter(status__name="completed", visibility="public").order_by(order_by)

    if user_id:
        submissions = submissions.filter(user=user_id)

    if mt:
        submissions = submissions.filter(model_type=MODEL_TYPE_MAP[mt])
        
    if not request.user.is_authenticated:
        return render(request, "leaderboard/logged_out_leaderboard.html", {"submissions": submissions})
    
    return render(request, "leaderboard/leaderboard.html", {"submissions": submissions, "authors": users, "modeltypes": MODEL_TYPE_CHOICES})
