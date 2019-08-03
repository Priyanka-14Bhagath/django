from django.shortcuts import render
from django.http import HttpResponse


def Home_Page(request):
    return HttpResponse("<h1 style='color:red;font-family:candara;font-size:40px;text-decoration:underline;"
                        "font-weight:border;'>Welcome to Django World....!!</h1>")


def Index(request):
    return HttpResponse("<h3 style>Hello.Sgdxgfhg..!!</h3>")


def Home(request):
    return HttpResponse("<b>GOOD BYE.....!!</b>")
