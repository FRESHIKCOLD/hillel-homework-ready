from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("name", "game", "quantity", "price", "created_at")
    list_filter = ("game", "created_at")
    search_fields = ("name", "description")
    list_editable = ("quantity", "price")
    ordering = ("name",)
