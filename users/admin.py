from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import EmployeeID


User = get_user_model()

admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):

    list_display = ["fullname", "username"]
    list_filter = ["is_active"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "fullname",
                    "username",
                    "designation",
                )
            },
        ),
        (
            ("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        (
            ("Balance"),
            {
                "fields": (
                    "salary",
                    "deducted_salary",
                    "final_salary",
                )
            },
        ),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.register(EmployeeID)
