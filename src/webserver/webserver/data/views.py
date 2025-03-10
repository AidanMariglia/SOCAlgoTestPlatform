from django.http import HttpRequest
from django.shortcuts import render

def data(request: HttpRequest):
    return render(request, "data.html")
