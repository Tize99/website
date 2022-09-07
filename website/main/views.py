from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def create1(request):
    return render(request, 'main/create1.html')
