from django.contrib import admin
from webapp.models import Emp
class EmpAdmin(admin.ModelAdmin):
    list_display = ['Name','Salary','Age']
admin.site.register(Emp,EmpAdmin)
# Register your models here.
