from django import forms


class SentForm(forms.Form):
    name = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows': 8,'cols':70}))

