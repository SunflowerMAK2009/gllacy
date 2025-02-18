from django import forms
from .models import Filler
class FilterForm(forms.Form):
    fat = forms.CharField(max_length=20, required=False)
    fillers = forms.MultipleChoiceField(choices=Filler.FILLER_CHOICES, required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
