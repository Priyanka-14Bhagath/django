from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_page(request):
    return HttpResponse("<h1>Welcome to Django world</h1>")
def Index(request):
    return HttpResponse("welecome to index page")
