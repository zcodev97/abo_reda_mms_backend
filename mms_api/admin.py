from django.contrib import admin
from .models import (Deposit, Withdraw,
                     Company, Container)


# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'container', 'total_dinar',
                    'total_dollar', 'created_at', 'created_by']


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_dinar', 'total_dollar',
                    'created_at', 'created_by']


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_id',
                    'container', 'company_name',
                    'price_in_dinar', 'price_in_dollar',
                    'description', 'received_from',
                    'created_at', 'created_by']


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_id',
                    'container', 'company_name', 'mr',
                    'price_in_dinar', 'price_in_dollar',
                    'description', 'out_to',
                    'created_at', 'created_by']

#
# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['timestamp', 'user',
#                     'action', 'details', 'model_affected','record_id']
