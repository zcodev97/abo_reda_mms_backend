from django.contrib import admin
from .models import (Deposit, Withdraw, WithdrawType,
                     Company, Container, EndpointLog)


# Register your models here.


@admin.register(EndpointLog)
class EndpointLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'path', 'method', 'action','status_code', 'timestamp']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'container', 'total_dinar',
                    'total_dollar', 'created_at', 'created_by']


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ['name'] # Fields to search by
    list_display = ['id', 'name', 'total_dinar', 'total_dollar',
                    'created_at', 'created_by']


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    # list_filter = ('container', 'company_name','description','received_from')  # Fields to filter by in the sidebar
    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('container__name', 'company_name__title','description','received_from') # Fields to search by

    list_display = [
        # 'id', 'invoice_id',
                    'container', 'company_name',
                    'price_in_dinar', 'price_in_dollar',
                    'description', 'received_from',
                    'created_at', 'created_by']


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ( 'withdraw_type__title',
                    'container__name', 'company_name__title','description','out_to') # Fields to search by
    list_display = ['id', 'invoice_id', 'withdraw_type',
                    'container', 'company_name',
                    'price_in_dinar', 'price_in_dollar',
                    'description', 'out_to',
                    'created_at', 'created_by']


@admin.register(WithdrawType)
class WithdrawTypeAdmin(admin.ModelAdmin):
    list_per_page = 5  # Items per page
    search_fields = ['title'] # Fields to search by
    list_display = ['id', 'title']

# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['timestamp', 'user',
#                     'action', 'details', 'model_affected','record_id']
