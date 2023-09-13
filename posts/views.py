from datetime import datetime

from django.shortcuts import render
# Create your views here.
from django.contrib.sites import requests
from django.http import HttpResponse


def greetings_views(requests):
    if requests == 'GET':
        return HttpResponse("hello my first project:)) there will be more to come")


def now_date(request):
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(current_date)

def goodby(request):
    return HttpResponse("Goodbye user!")
