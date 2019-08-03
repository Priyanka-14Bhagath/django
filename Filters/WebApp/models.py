from django.db import models

# Create your models here.


class Filter(models.Model):
    Name = models.CharField(max_length=30)
    Subject = models.CharField(max_length =30)
    Dept = models.CharField(max_length =30)
    Date = models.DateField()
