# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def Hits_view(request):
    hit=request.COOKIES.get('hit',0)
    newhit = int(hit)+1
    response = render(request,'hits.html',{'hit':newhit})
    response.set_cookie('hit',newhit)
    return response
def Hits_view(request):
    hit=request.COOKIES.get('hit',0)
    newhit = int(hit)+1
    response = render(request,'hits.html',{'hit':newhit})
    response.set_cookie('hit',newhit)
    return response
# Create your views here.
