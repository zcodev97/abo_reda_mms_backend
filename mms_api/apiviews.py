from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .models import Container, Company, Deposit, Withdraw
from .serializers import (ContainerSerializer,
                          CompanySerializer,CompanyCreateSerializer,
                          DepositSerializer,DepositCreateSerializer, WithdrawSerializer,WithdrawCreateSerializer)
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


class ContainerAPI(generics.ListCreateAPIView):
    queryset = Container.objects.all()
    serializer_class = ContainerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class CompaniesListAPI(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class CompanyCreateAPI(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]


class DepositAPI(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class DepositCreateAPI(generics.CreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositCreateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class WithdrawAPI(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class WithdrawCreateAPI(generics.CreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawCreateSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class ContainerDepositAPI(generics.ListCreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Assuming you get the container_id from the request's query parameters

        container_id = self.kwargs['pk']
        print(container_id)
        if container_id:
            # If container_id is provided, filter deposits for that specific container
            queryset = Deposit.objects.filter(container__id=container_id)
        else:
            # If no container_id is provided, return all deposits
            queryset = Deposit.objects.all()

        return queryset


class ContainerWithdrawsAPI(generics.ListCreateAPIView):
    serializer_class = WithdrawSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Assuming you get the container_id from the request's query parameters
        container_id = self.kwargs['pk']

        if container_id:
            # If container_id is provided, filter deposits for that specific container
            queryset = Withdraw.objects.filter(container__id=container_id)
        else:
            # If no container_id is provided, return all deposits
            queryset = Withdraw.objects.all()


        return queryset


class CompanyDepositAPI(generics.ListCreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        company_name_id = self.kwargs['pk']
        print( self.request)
        if company_name_id:
            # If container_id is provided, filter deposits for that specific container
            queryset = Deposit.objects.filter(company_name_id=company_name_id)
        else:
            # If no container_id is provided, return all deposits
            queryset = Deposit.objects.all()
        return queryset


class CompanyWithdrawsAPI(generics.ListCreateAPIView):
    serializer_class = WithdrawSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # Assuming you get the container_id from the request's query parameters
        company_name_id = self.kwargs['pk']

        if company_name_id:
            # If container_id is provided, filter deposits for that specific container
            queryset = Withdraw.objects.filter(company_name_id=company_name_id)
        else:
            # If no container_id is provided, return all deposits
            queryset = Withdraw.objects.all()

        return queryset
