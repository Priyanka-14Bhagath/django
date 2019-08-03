# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


# Create your views here.
@login_required
def Home_page(request):
    return render(request,'home.html')

def Customer_page(request):
    return render(request,'customer.html')

def Login_page(request):
    return render(request,'registration/login.html')

def Logout_page(request):
    return render(request,'logout.html')

