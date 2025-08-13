from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


User = get_user_model()


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User

    # Fields shown in the user list view
    list_display = ("full_name", "email", "date_of_birth", "is_agent")
    list_filter = ("is_agent", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "date_of_birth")}),
        (_("Permissions"),
         {"fields": ("is_agent", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name", "last_name", "email", "password1", "password2", "date_of_birth", "is_agent", "is_staff",
                "is_active"),
        }),
    )

    search_fields = ("first_name", "last_name", "email")
    ordering = ("last_name", "first_name")


# Register the model and custom admin
admin.site.register(User, CustomUserAdmin)
