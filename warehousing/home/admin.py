from django.contrib import admin
from .models import TransferItem, Transfer


class TransferItemInline(admin.TabularInline):
    model = TransferItem


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    inlines = (TransferItemInline, )
