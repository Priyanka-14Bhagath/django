from django.shortcuts import render
from django.http import HttpResponse


def Home_Page(request):
    return HttpResponse("Welcome to Django World....!!")

# Create your views here.
