from django.contrib import admin

# Register your models here.
from .models import EngineeringRequest, EngineeringRequestItem, EngineeringService


@admin.register(EngineeringService)
class EngineeringServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "display_order"]
    search_fields = ["name", "code"]


class EngineeringRequestItemInline(admin.TabularInline):
    model = EngineeringRequestItem
    extra = 1


@admin.register(EngineeringRequest)
class EngineeringRequestAdmin(admin.ModelAdmin):
    list_display = ["id", "room", "assigned_to", "status", "completed_at", "created_at"]
    list_filter = ["status", "created_at", "completed_at"]
    search_fields = ["room__room_number", "assigned_to__username"]
    inlines = [EngineeringRequestItemInline]
