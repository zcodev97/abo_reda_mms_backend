from django.contrib import admin
from .models import (Deposit, Withdraw, WithdrawType,
                     Company, Container)
from django.utils.html import format_html


# Register your models here.


# @admin.register(EndpointLog)
# class EndpointLogAdmin(admin.ModelAdmin):
#     list_display = ['user', 'path', 'method', 'action','status_code', 'timestamp']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")
    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = [ 'title', 'container', 'formatted_total_price_dinar',
                    'formatted_total_price_dollar', 'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(CompanyAdmin,self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions



@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):


    def formatted_total_price_dinar(self, obj):
        return format_html(f"IQD {obj.total_dinar:,.0f}")
    def formatted_total_price_dollar(self, obj):
        return format_html(f"$ {obj.total_dollar:,.0f}")

    formatted_total_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_total_price_dollar.short_description = 'Total Dollar'  # Sets the column header


    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ['name'] # Fields to search by
    list_display = [ 'name', 'formatted_total_price_dinar', 'formatted_total_price_dollar',
                    'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(ContainerAdmin,self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    # list_filter = ('container', 'company_name','description','received_from')  # Fields to filter by in the sidebar
    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ('container__name', 'company_name__title','description','received_from') # Fields to search by


    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")
    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header

    list_display = [
        # 'id', 'invoice_id',
                    'container', 'company_name',
                    'formatted_price_dinar', 'formatted_price_dollar',
                    'description', 'received_from',
                    'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(DepositAdmin,self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):

    def formatted_price_dinar(self, obj):
        return format_html(f"IQD {obj.price_in_dinar:,.0f}")
    def formatted_price_dollar(self, obj):
        return format_html(f"$ {obj.price_in_dollar:,.0f}")

    formatted_price_dinar.short_description = 'Total Dinar'  # Sets the column header

    formatted_price_dollar.short_description = 'Total Dollar'  # Sets the column header



    list_per_page = 5  # Items per page
    ordering = ('-created_at',)  # Default ordering
    search_fields = ( 'withdraw_type__title',
                    'container__name', 'company_name__title','description','out_to') # Fields to search by
    list_display = [ 'invoice_id', 'withdraw_type',
                    'container', 'company_name',
                    'formatted_price_dinar', 'formatted_price_dollar',
                    'description', 'out_to',
                    'created_at', 'created_by']

    def get_actions(self, request):
        actions = super(WithdrawAdmin,self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.register(WithdrawType)
class WithdrawTypeAdmin(admin.ModelAdmin):
    list_per_page = 5  # Items per page
    search_fields = ['title'] # Fields to search by
    list_display = [ 'title']

    def get_actions(self, request):
        actions = super(WithdrawTypeAdmin,self).get_actions(request)
        print(actions)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


# @admin.register(LogEntry)
# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['timestamp', 'user',
#                     'action', 'details', 'model_affected','record_id']
