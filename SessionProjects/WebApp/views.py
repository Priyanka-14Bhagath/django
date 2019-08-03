from django.http import HttpResponse
from django.shortcuts import render


def Hits_View(request):
    hit = request.session.get('hit', 0)
    newhit = int(hit)+1
    request.session['hit'] = newhit
    print("Session Expired Age :", request.session.get_expiry_age())
    print("Session Expired Date :", request.session.get_expiry_date())
    return render(request, 'MyApp/Session.html', {'hit': newhit})


