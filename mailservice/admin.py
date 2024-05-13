from django.contrib import admin

from mailservice.models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "email")
    list_filter = ("name",)
    search_fields = ("name", "email", "comments")
