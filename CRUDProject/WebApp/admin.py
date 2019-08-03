from django.contrib import admin
from WebApp.models import company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','company_logp','company_city']

admin.site.register(company,CompanyAdmin)
