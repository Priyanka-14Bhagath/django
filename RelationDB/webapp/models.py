from django.db import models

# Create your models here.
class State(models.Model):
    sname=models.CharField(max_length=255)
    def __str__(self):
        return self.sname
class CapitalCity(models.Model):
    cname=models.CharField(max_length=255,primary_key=True)
    State=models.OneToOneField(State,on_delete=models.CASCADE,)
    def __str__(self):
        return self.cname