from django import forms
from webapp.models import Emp
class EmpForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = '_all_'