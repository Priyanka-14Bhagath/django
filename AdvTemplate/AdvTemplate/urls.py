"""AdvTemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from WebApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home/', views.Home_Page),
    path('Admin/', views.Admin_Page),
    path('Backup/', views.Backup_Page),
    path('Help/', views.Help_Page),
    path('Menu/', views.Menu_Page),
    path('StudentDetails/', views.Student_Details_Page),
    path('View/', views.View_Page),
    path('Windows/', views.Windows_Page),
]
