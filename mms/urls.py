from django.contrib import admin
from django.urls import path
from mms_api.apiviews import (ContainerAPI,
                              CompaniesListAPI,CompanyCreateAPI,
                              DepositAPI,
                              DepositCreateAPI,
                              WithdrawAPI,
                              ContainerDepositAPI,
                              ContainerWithdrawsAPI,
                              CompanyWithdrawsAPI,
                              CompanyDepositAPI,
                              WithdrawCreateAPI,WithdrawsReportAPI,DepositsReportAPI,
                              WithdrawTypeAPI,CreateWithdrawTypeAPI)
from core.serializers import CustomUserSerializer
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Assuming you have a serializer for your user model
        user_serializer = CustomUserSerializer(self.user).data
        data.update({'user': user_serializer})
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


urlpatterns = [
    path('admin/', admin.site.urls),
    # mms api
    path('containers/', ContainerAPI.as_view(), name="ContainerAPI"),
    path('companies/', CompaniesListAPI.as_view(), name="list companies"),
    path('company_create/', CompanyCreateAPI.as_view(), name="create company"),
    path('deposits/', DepositAPI.as_view(), name="deposits"),
    path('create_deposit/', DepositCreateAPI.as_view(), name="create deposit"),
    path('withdraws/', WithdrawAPI.as_view(), name="withdraw"),
    path('withdraws_report/', WithdrawsReportAPI.as_view(), name="withdraws report"),
    path('deposits_report/', DepositsReportAPI.as_view(), name="deposits report"),
    path('create_withdraw/', WithdrawCreateAPI.as_view(), name="create withdraw"),
    path('withdraw_types/', WithdrawTypeAPI.as_view(), name="fetch all withdraw types"),
    path('create_withdraw_type/', CreateWithdrawTypeAPI.as_view(), name="create withdraw type"),

    path('container_deposits/<uuid:pk>', ContainerDepositAPI.as_view(), name="container deposits"),
    path('container_withdraws/<uuid:pk>', ContainerWithdrawsAPI.as_view(), name="container withdraws"),
    path('company_deposits/<uuid:pk>', CompanyDepositAPI.as_view(), name="container deposits"),
    path('company_withdraws/<uuid:pk>', CompanyWithdrawsAPI.as_view(), name="container withdraws"),

    # login
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
