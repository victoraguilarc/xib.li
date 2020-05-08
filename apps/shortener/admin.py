# -*- coding: utf-8 -*-

from django.contrib import admin
from apps.accounts.models.pending_action import PendingAction
from apps.shortener.models import Link


@admin.register(Link)
class Linkdmin(admin.ModelAdmin):
    """Defines the Link admin behaviour."""

    raw_id_fields = ('owner', )
    list_display = (
        'url',
        'alias',
        'clicks_count',
        'owner',
        'created_at',
    )
