from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import Container, Company, Deposit, Withdraw, WithdrawType

from core.serializers import CustomUserSerializer


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ('id', 'name', 'total_dinar', 'total_dollar', 'created_at', 'created_by')


class WithdrawTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithdrawType
        fields = ('id', 'title')


class CompanySerializer(serializers.ModelSerializer):
    container = ContainerSerializer()

    class Meta:
        model = Company
        fields = ['id', 'title', 'container', 'total_dinar','supervisor',
                  'total_dollar', 'created_by', 'created_at', 'created_by']


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['title', 'container','supervisor', 'total_dinar', 'total_dollar', 'created_by']


class DepositSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()
    container = ContainerSerializer()

    class Meta:
        model = Deposit
        fields = ['invoice_id','deposit_number', 'container', 'company_name', 'price_in_dollar',
                  'price_in_dinar', 'description',
                  'received_from', 'created_at','document']


class DepositCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ['invoice_id', 'container', 'company_name', 'price_in_dollar',
                  'price_in_dinar', 'description',
                  'received_from', 'created_at', 'created_by','document']


class WithdrawSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()
    container = ContainerSerializer()
    withdraw_type = WithdrawTypeSerializer()

    class Meta:
        model = Withdraw
        fields = ['invoice_id', 'withdraw_number', 'container', 'company_name', 'price_in_dollar',
                  'price_in_dinar', 'description',
                  'out_to', 'withdraw_type', 'created_at','document']


class WithdrawCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ['container', 'company_name', 'price_in_dollar',
                  'price_in_dinar', 'description',
                  'out_to', 'withdraw_type', 'created_at', 'created_by','document']
