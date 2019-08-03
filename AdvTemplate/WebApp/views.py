from django.shortcuts import render

# Create your views here.


def Home_Page(request):
    return render(request, 'MyApp/Home.html')


def Admin_Page(request):
    return render(request, 'MyApp/Admin.html')


def Backup_Page(request):
    return render(request, 'MyApp/Backup.html')


def Help_Page(request):
    return render(request, 'MyApp/Help.html')


def Menu_Page(request):
    return render(request, 'MyApp/Menu.html')


def Student_Details_Page(request):
    return render(request, 'MyApp/StudentDetails.html')


def View_Page(request):
    return render(request, 'MyApp/View.html')


def Windows_Page(request):
    return render(request, 'MyApp/Windows.html')

