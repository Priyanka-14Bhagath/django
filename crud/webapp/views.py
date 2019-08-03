from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from.models import companytable
from.forms import NewForm
# Create your views here.


def home(request):
    orglist=companytable.objects.all()
    return render(request,'home.html', {'orglist': orglist})


def org_create(request):
    form = NewForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance = form.save()
        instance.save()
        return HttpResponseRedirect('/')
    context = {'form':form}
    return render(request,'create.html',context)