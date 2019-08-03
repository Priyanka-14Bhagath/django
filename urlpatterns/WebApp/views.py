from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page(request):
    return HttpResponse("<h1> Welcome to Home Page</h1>")
def Index_page(request):
    return HttpResponse('welcome to Index Page of')
def Hello_page(request):
    return HttpResponse('<h3>welcome to Hello Page of</h3>')
def MyTempView(request):
    return render(request,'Welcome.html')