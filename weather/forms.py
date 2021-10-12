from django import forms
from django.forms import TextInput


class CityForm(forms.Form):
    city = forms.CharField(required=True)


class ArchiveForm(forms.Form):
    city = forms.CharField(required=False)
    date_from = forms.DateField(required=False, help_text='yyyy-mm-dd')
    date_to = forms.DateField(required=False, help_text='yyyy-mm-dd')


class ForecastForm(forms.Form):
    city = forms.CharField(required=True)
