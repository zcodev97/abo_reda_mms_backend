from django.conf import settings
# from .models import User
from rest_framework import serializers
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import User, UserType


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = ['id', "title"]


class CustomUserSerializer(serializers.ModelSerializer):
    user_type = UserTypeSerializer()

    # department = serializers.CharField(source='department.name')
    # directorate = serializers.CharField(source='directorate.name')
    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'first_name', 'last_name',
                  'is_superuser', "user_type"]
