from django.forms import ModelForm
from django import forms
from .models import Product

class AddProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'image',
            'category'
        ]



