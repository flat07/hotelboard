# backend/hk/filters.py
import django_filters

from hk.models import HousekeepingRequest


class HousekeepingRequestFilter(
    django_filters.FilterSet,
):
    status = django_filters.CharFilter()

    room = django_filters.CharFilter(
        field_name="room__number",
        lookup_expr="icontains",
    )

    assigned_to = django_filters.CharFilter(
        field_name="assigned_to__username",
        lookup_expr="icontains",
    )

    class Meta:
        model = HousekeepingRequest

        fields = [
            "status",
            "room",
            "assigned_to",
        ]
