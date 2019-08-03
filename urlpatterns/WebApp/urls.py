from django.urls import path
from WebApp import views
from django.contrib import admin


urlpatterns=[
    path('Index/',views.Index_page),
    path('hello/',views.Hello_page),
    path('admin/',admin.site.urls),
    path('temp/',views.MyTempView),
]