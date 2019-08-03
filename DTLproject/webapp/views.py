from django.shortcuts import render
from datetime import datetime
from webapp import forms
from requests.api import request
def Template_Django(request):
    import datetime
    date=datetime.datetime.now()
    name="NareshIT"
    MyDic={'dt':date,'name':name}
    return render(request,'welcomedtl.html',MyDic)
def Template_Djangoo(request):
    date_now=datetime.now()
    name="NareshIT"
    th=int(date_now.strftime('%H'))
    if th<12:
        txt="good morning"
    elif th<16:
        txt="good evening"
    else:
        txt="good night"
    my_dict={'date_now':date_now,'name':name,'txt':txt}
    return render(request,'datetime.html',my_dict)
def images(request):
    import datetime
    date = datetime.datetime.now()
    name = "NareshIT"
    MyDic = {'dt': date, 'name': name}
    return render(request, 'image.html', MyDic)
def EmpView(request):
    form=forms.EmpForm(request.POST)
    if form.is_valid():
        print("validations are success Folks!!!")
        print(form.cleaned_data['Name'])
        print(form.cleaned_data['Salary'])
    return render(request,'forms.html',{'form':form})

def ThankView(request):
    form = forms.EmpForm()
    MyDict = {'form':form }
    return render(request,'Thanks.html')

def EmpVieww(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
                print("validations are success Folks!!!")
                print(form.cleaned_data['Name'])
                print(form.cleaned_data['Salary'])
                print(form.cleaned_data['opinion'])
    return render(request, 'register.html', {'form': form})



def EmpViewww(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
                print("welcome to validations!!!")
                print(form.cleaned_data['Name'])
                print(form.cleaned_data['Salary'])
                print(form.cleaned_data['Age'])
                print(form.cleaned_data['Address'])

                print(form.cleaned_data['Opinion'])
        #return HttpResponseRedirect('/Bye')
    else:
        form=forms.EmpForm()
    return render(request, 'register.html', {'form': form})



# Create your views here.
