from django import forms
from django.core import validators



def Begin_with_S(value):
    if value[0]!='S':
        raise forms.ValidationError("Name Must Start with 'S' .")
def Begin_with_Alpha(value):
    if value.isalpha()!= True:
        raise forms.ValidationError("Must Be Character")


class EmpForm(forms.Form):
    Name = forms.CharField(validators=[Begin_with_S,Begin_with_Alpha])
    Salary = forms.IntegerField()
    Email_Id = forms.EmailField()
    Opinion = forms.CharField(widget=forms.Textarea,validators= [validators.MaxLengthValidator(30),validators.MinLengthValidator(10)])
    Bot_Field = forms.CharField(required= False,widget=forms.HiddenInput)
    def clean(self):
        print("Welcome to ROBOT Validation")
        cdata = super().clean()
        bhandle = cdata['Bot_Field']
        if len(bhandle) > 0:
            raise forms.ValidationError("Hei BOT ,Unable to Process")

