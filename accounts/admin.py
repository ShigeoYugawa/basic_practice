from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """CustomUser用の管理画面"""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "nickname", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "nickname")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "nickname", "password")}),
        ("権限情報", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("重要な日付", {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "nickname", "password1", "password2", "is_staff", "is_active")}
        ),
    )
