from django.shortcuts import render
import datetime
# Create your views here.


def Template_Django(request):
    date = datetime.datetime.now()
    name = "Django"
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        data = "Good Morning"
    elif 12 <= hour < 16:
        data = "Good Afternoon"
    elif 16 <= hour < 18:
        data = "Good Evening"
    else:
        data = "Good Night"
    Mywish = {"dt": date , "name": name , "daywish": data}
    return render(request,'MyApp/Welcome.html', Mywish)


def wishMe(request):
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        data = "Good Morning"
    elif 12 <= hour < 16:
        data = "Good Afternoon"
    elif 16 <= hour < 18:
        data = "Good Evening"
    else:
        data = "Good Night"
    wish_my = {"wish": data}
    return render(request, 'MyApp/Welcome.html', wish_my)
