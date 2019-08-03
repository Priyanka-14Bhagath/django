from django.shortcuts import render
# Create your views here.

def MyTempViews(request):
    return render(request, 'MyApp/welcome.html')
