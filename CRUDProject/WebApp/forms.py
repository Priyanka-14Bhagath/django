from .models import company
from django import forms

class NewForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['company_name','company_logp','company_city']