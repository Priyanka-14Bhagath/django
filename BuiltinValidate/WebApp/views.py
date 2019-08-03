from django.shortcuts import render
from requests.api import request
from WebApp import forms
from django.http import HttpResponseRedirect
# Create your views here.

#
# def EmpView(request):
#     form = forms.EmpForm()
#     MyDict = {'form': form}
#     return render(request,'MyApp/Welcome.html', MyDict)

def ThankView(request):
    form = forms.EmpForm()
    MyDict = {'form': form}
    return render(request,'MyApp/Thanks.html', MyDict)


def EmpView(request):
    form = forms.EmpForm()
    if request.method=='POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            print("Validations are success folks..!!")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            print(form.cleaned_data['Bot_Field'])
            return HttpResponseRedirect('/Bye')
    # if request.method=='GET':
    #     MyDict = {'form': form}
    #     return render(request, 'MyApp/Register.html', MyDict)
    else:
        form = forms.EmpForm()
    MyDict = {'form': form}
    return render(request,'MyApp/Register.html', MyDict)




