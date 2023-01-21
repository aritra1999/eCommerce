from django import forms
from django.forms import ModelForm
from .models import Address
from billing.models import BillingProfile
from django.conf import settings

User = settings.AUTH_USER_MODEL
class AddressForm(forms.ModelForm):


    class Meta:
        model = Address
        fields = [
            'address_line_1',
            'address_line_2',
            'city',
            'country',
            'state',
            'phone_no',
            'postal_code'
        ]

        labels = {
            'address_line_1': 'Address 1',
            'address_line_2': 'Address 2 (Optional)',
        }
        widgets = {
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 1'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address line 2'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter city'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter postal code'}),
        }
