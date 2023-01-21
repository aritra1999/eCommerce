from django.forms import ModelForm
from .models import Store
from django import forms


class StoreRegistrationForm(forms.ModelForm):
    class Meta:
        model = Store
        exclude = {
            'owner'
        }
        fields = [
            'store_name',
            'address',
            'city',
            'country',
            'state',
            'postal_code',
        ]
        widgets = {
            'store_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }


# store_name = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your store name"}))
    # store_address = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your stores address"}))
    # city = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City?"}))
    # country = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Country?"}))
    # state = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "State?"}))
    # postal_code = forms.CharField(
    #     widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Postal Code?"}))

