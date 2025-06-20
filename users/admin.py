from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = (
        "id",
        "email",
        "username",
        "country",
        "is_staff",
        "is_active",
    )  # Added country
    list_filter = ("is_staff", "is_superuser", "is_active")
    search_fields = ("email", "username", "country")  # Optional
    ordering = ("id",)

    fieldsets = (
        (
            None,
            {"fields": ("email", "username", "password", "country")},
        ),  # Added country
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "country",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },  # Added country
        ),
    )


admin.site.register(User, UserAdmin)
