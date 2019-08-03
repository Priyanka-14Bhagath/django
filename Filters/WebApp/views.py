from django.shortcuts import render
from WebApp.models import Filter

# Create your views here.


def FilterView(request):
    FilterList = Filter.objects.all()
    return render(request, 'MyApp/Welcome.html', {'FilterList': FilterList})

def Template_Django(request):

    return render(request,'MyApp/Home_Page.html')

