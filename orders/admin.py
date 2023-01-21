from django.contrib import admin

from .models import Order, Placed

admin.site.register(Order)
admin.site.register(Placed)
