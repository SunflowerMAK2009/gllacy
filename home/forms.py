from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(required=True)

class PopupForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    comment = forms.CharField(max_length=200, required=False)

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False)