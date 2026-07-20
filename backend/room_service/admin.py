from django.contrib import admin

from .models import MenuCategory, MenuItem, RoomServiceOrder, RoomServiceOrderItem


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "display_order"]
    search_fields = ["name"]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price", "is_available", "display_order"]
    list_filter = ["category", "is_available"]
    search_fields = ["name"]


class RoomServiceOrderItemInline(admin.TabularInline):
    model = RoomServiceOrderItem
    extra = 1


@admin.register(RoomServiceOrder)
class RoomServiceOrderAdmin(admin.ModelAdmin):
    list_display = ["id", "room", "assigned_to", "status", "total_price", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["room__room_number", "assigned_to__username"]
    inlines = [RoomServiceOrderItemInline]
