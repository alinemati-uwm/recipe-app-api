"""
Django admin customization for the app.

"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin model for custom User model with no email field."""

    ordering = ["id"]
    list_display = ["email", "name"]
    list_filter = ["is_active", "is_staff"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff")}),
        ("Personal", {"fields": ("name",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )

admin.site.register(models.User, UserAdmin) 