from django.http import HttpResponse
from django.shortcuts import render


# def Test_Cookie(request):
#     request.session.set_test_cookie()
#     return HttpResponse("Welcome To Cookies...!!")
#
#
# def Check_Cookie(request):
#     if request.session.test_cookie_worked():
#         print("Cookies are working Perfectly")
#     return HttpResponse("Cookies are working Perfectly")


# def Hits_View(request):
#     hit = request.COOKIES.get('hit',0)
#     newhit = int(hit)+1
#     response = render(request,'MyApp/Welcome.html', {'hit':newhit})
#     response.set_cookie('hit',newhit)
#     return response

def Hits_View(request):
    hit = request.session.get('hit',0)
    newhit = int(hit)+1
    request.session['hit'] = newhit
    print("Session Expired Age :", request.session.get_expiry_age())
    print("Session Expired Date :", request.session.get_expiry_date())
    return render(request,'MyApp/Welcome.html', {'hit':newhit})


