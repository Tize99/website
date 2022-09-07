from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h4>Hello</h4>")


def index2(request):
    return HttpResponse("<h4>Hello, Django!</h4>")
