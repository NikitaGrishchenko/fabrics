from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group as BaseGroup

from .models import ProxyGroup, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "patronymic",
        "phone",
        "is_staff",
    )
    list_readonly_not_superuser_fields = (
        "is_superuser",
        "is_staff",
        "last_login",
        "date_joined",
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Персональная информация"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "patronymic",
                    "email",
                    "phone",
                )
            },
        ),
        (
            ("Права"),
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
        (("Активность"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.unregister(BaseGroup)
admin.site.register(ProxyGroup, GroupAdmin)