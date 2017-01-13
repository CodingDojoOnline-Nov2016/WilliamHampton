from django.shortcuts import render
from . import models

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
