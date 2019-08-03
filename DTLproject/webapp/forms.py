from django import forms
from django.core import validators

def Begin_with_S(value):
    if value[0]!='S':
        raise forms.ValidationError("Name must start with  S ")
    if value[0]!='10':
        raise forms.ValidationError("Age must start with  10 ")



class EmpForm(forms.Form):
    Name = forms.CharField(validators=[Begin_with_S])
    Salary = forms.IntegerField()
    Bot_Field = forms.CharField(required=False, widget=forms.HiddenInput)
    def clean(self):
        print("Welcome to ROBOT validations")
        cdata = super().clean()
        bhandel = cdata['Bot_Field']
        if len(bhandel)>0:
            raise forms.ValidationError("Hei Bot,Unable to process")


