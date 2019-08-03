from django.db import models
from django.urls import reverse

# Create your models here.
class companytable(models.Model):
    Company_name = models.CharField(max_length=40)
    Company_logo = models.FileField(null='True' , blank = 'True')
    Company_city = models.CharField(max_length=40)