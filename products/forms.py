from django.forms import ModelForm
from django import forms
from .models import Product

CATEGORY = (
    ('jewellery', 'Jewellery'),
    ('homedecor', 'Home Decor'),
    ('clothing', 'Clothing'),
)


class AddProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        exclude = {'seller', 'store_name'}
        fields = [
            'title',
            'description',
            'price',
            'image',
            'color',
            'category',
        ]
        labels = {
            'title': 'Enter product name',
            'image': 'Choose file',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product Name'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter product description / details'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product price'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': 'Choose Image'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product color'}),
            'category': forms.Select(choices=CATEGORY,
                                     attrs={'class': 'form-control', 'placeholder': 'Enter Product color'})
        }
