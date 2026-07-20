from django.contrib import admin

from .models import HousekeepingRequest, HousekeepingRequestItem, HousekeepingService


@admin.register(HousekeepingService)
class HousekeepingServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "display_order"]
    search_fields = ["name", "code"]


class HousekeepingRequestItemInline(admin.TabularInline):
    model = HousekeepingRequestItem
    extra = 1


@admin.register(HousekeepingRequest)
class HousekeepingRequestAdmin(admin.ModelAdmin):
    list_display = ["id", "room", "assigned_to", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["room__room_number", "assigned_to__username"]
    inlines = [HousekeepingRequestItemInline]
