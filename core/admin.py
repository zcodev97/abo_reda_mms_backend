from django.contrib import admin
from .models import User,UserType
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email","user_type")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username", "password1", "password2",
                    "email", "first_name", "last_name","user_type"),
            },
        ),
    )
    list_display = ['id', 'username', 'user_type', 'first_name',
                    'last_name', 'email', 'is_superuser']

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ['id','title']
