from django import forms
class School(forms.Form):
    Sname=forms.CharField()
    Sprincipal=forms.CharField()
    Slocation=forms.CharField()