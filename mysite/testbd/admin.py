from django.contrib import admin
from .models import Purchase, Transaction
# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    fields = ['type']

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Purchase)