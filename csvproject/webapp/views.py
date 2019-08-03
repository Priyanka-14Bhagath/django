from django.shortcuts import render
from django.http import HttpResponse
import csv
def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['ContentDisposition']='attachment;filename ="BigData.csv"'
    writer = csv.writer(response)
    writer.writerow(['1001','SUbba','Raju','s/w'])
    writer.writerow(['1002','sara','Thomson','network',"'Testing'"])
    writer.writerow(['1003','smith','john','h/w'])
    return response

# Create your views here.
