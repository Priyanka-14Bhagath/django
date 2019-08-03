from django.shortcuts import render

# Create your views here.


def MyTempViews(request):
    return render(request, 'MyApp/Welcome.html')


def WebTempViews(request):
    return render(request, 'MyApp/web_temp.html')

