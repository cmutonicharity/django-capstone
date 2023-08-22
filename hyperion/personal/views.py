from django.shortcuts import render

# personal/views.py
from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, 'about.html')


def work(request):
    return render(request, 'work.html')


def fun(request):
    return render(request, 'fun.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
