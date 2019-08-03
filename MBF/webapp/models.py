from django.db import models
class Emp(models.Model):
    Name= models.CharField(max_length=30)
    Salary = models.IntegerField()
    Age = models.IntegerField()

# Create your models here.
