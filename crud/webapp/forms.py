from.models import companytable
from django import forms
class NewForm(forms.ModelForm):
    class Meta:
        model = companytable
        fields=[
            'Company_name',
            'Company_logo',
            'Company_city',
        ]
