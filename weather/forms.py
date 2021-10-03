from django import forms


class CityForm(forms.Form):
    city = forms.CharField(required=True)


class ArchiveForm(forms.Form):
    city = forms.CharField(required=False)
    date_from = forms.DateField(required=False)
    date_to = forms.DateField(required=False)
