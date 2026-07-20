from django.contrib import admin

from .models import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ["room_number", "floor", "room_type", "is_active"]
    list_filter = ["room_type", "is_active", "floor"]
    search_fields = ["room_number"]
    readonly_fields = ["public_token"]
