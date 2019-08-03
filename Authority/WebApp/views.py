from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def Customer(request):
    return render(request,'MyApp/customer.html')


def Home_Page(request):
    return render(request,'MyApp/home.html')


def Login_Page(request):
    return render(request,'registration/login.html')


def Logout_Page(request):
    return render(request,'MyApp/logout.html')


