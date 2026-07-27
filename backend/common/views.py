# backend/common/views.py
from django.core.cache import cache
from django.db import connection
from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok"})


def readiness(request):
    connection.ensure_connection()
    cache.set("ready", "1", timeout=5)

    return JsonResponse({"status": "ready"})
