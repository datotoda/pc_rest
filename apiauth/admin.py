from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apiauth.models import ActivationToken

UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name', 'is_active')


@admin.register(ActivationToken)
class ActivationTokenAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('user',)}),
    )

