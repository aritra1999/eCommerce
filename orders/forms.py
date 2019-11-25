from django import forms
from .models import Placed

class PlacedForm(forms.ModelForm):
    class Meta:
        model = Placed
        exclude = {'product', 'store', 'buyer_address'}
        fields = []

