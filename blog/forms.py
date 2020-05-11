from django import forms
from django.core.exceptions import ValidationError


class search_forms(forms.Form):
    search = forms.TextInput()
    

    