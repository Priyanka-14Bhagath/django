from django.shortcuts import render
from.models import State
# Create your views here.
def statelist(request):
    items = State.objects.all()
    return render(request,'state.html',{'items':items})