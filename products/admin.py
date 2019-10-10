from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','price', 'slug','active','color','category','image','seller']
    # list_display = ['__str__','price', 'slug','active','color','category','image']

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)