from django import forms

class MyForm(forms.Form):
    color = forms.CharField()
    speed = forms.IntegerField()
    model = forms.CharField()
    tags = forms.CharField()