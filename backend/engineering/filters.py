import django_filters

from .models import EngineeringRequest


class EngineeringRequestFilter(django_filters.FilterSet):
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
        model = EngineeringRequest
        fields = [
            "status",
            "room",
            "assigned_to",
        ]
