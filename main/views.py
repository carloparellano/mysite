from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>carlo is learning Django!</h1>")

def v1(response):
    return HttpResponse("<h1>view 1!</h1>")