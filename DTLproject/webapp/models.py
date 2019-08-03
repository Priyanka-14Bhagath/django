from django.db import models

class Emp(models.Model):
    EmpId = models.IntegerField()
    EmpName = models.CharField(max_length=30)
    EmpSal = models.IntegerField()
    EmpAdd = models.CharField(max_length=30)
# Create your models here.
