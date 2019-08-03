from django.contrib import admin
from WebApp.models import Filter

# Register your models here.


class FilterAdmin(admin.ModelAdmin):
    list_display = ['Name', 'Subject', 'Dept', 'Date']


admin.site.register(Filter,FilterAdmin)


