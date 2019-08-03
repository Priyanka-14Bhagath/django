from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def  ThankView(request):
    return render(request,'Thanks.html')
def Emp_View(request):
    form=forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/bye')
    else:
        form = forms.EmpForm()
    return  render(request,'Registration.html',{'form':form})

# Create your views here.
def Home_page(request):
    return render(request,'home.html')
def courses_page(request):
    return render(request,'courses.html')
def training_page(request):
    return render(request,'training.html')


def Test_cookie(request):
    request.session.set_test_cookie()
    return HttpResponse("welcome to cookie")
def check_cookie(request):
    if request.session.set_test_cookie_worked():
        print("cookies are working perfectly")