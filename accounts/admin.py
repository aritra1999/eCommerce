from django.contrib import admin
from .models import GuestEmail, Account

class AccountAdmin(admin.ModelAdmin):
    list_display = ['__str__','name','email', 'date_joined','last_login','user_type']
    class Meta:
        model = Account

admin.site.register(GuestEmail)
admin.site.register(Account, AccountAdmin)