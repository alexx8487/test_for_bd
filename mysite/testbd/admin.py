from django.contrib import admin
from .models import Purchase, Transaction
# Register your models here.

admin.site.register(Transaction)
admin.site.register(Purchase)