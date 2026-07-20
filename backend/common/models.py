# backend/core/models.py

from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def inactive(self):
        return self.filter(is_active=False)


class ActiveManager(models.Manager.from_queryset(ActiveQuerySet)):
    pass


class ActivatableModel(models.Model):
    is_active = models.BooleanField(default=True)

    objects = ActiveManager()

    class Meta:
        abstract = True
