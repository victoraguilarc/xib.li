# -*- coding: utf-8 -*-

from urllib.parse import urlparse

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from apps.contrib.models import TimeStampedModelMixin, UUIDPrimaryKeyModelMixin


class Link(TimeStampedModelMixin, models.Model):
    owner = models.ForeignKey(
        'accounts.User',
        verbose_name=_('Owner'),
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='links',
    )
    url = models.URLField(max_length=2048)
    alias = models.CharField(
        max_length=255,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-z0-9-_]+$',
                code='invalid_alias',
                message=_('Alias can only contain lowercase alphabets, numerals, underscores and hyphens'),
            ),
        ]
    )
    clicks_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{0} -> {1}'.format(self.alias, self.url)

    def get_long_url_truncated(self, max_length=30, remove_schema=True):
        truncated_url = self.url
        if remove_schema:
            parsed_url = urlparse(truncated_url)
            scheme = parsed_url.scheme
            truncated_url = truncated_url[len(scheme)+3:]
            if parsed_url.path == '/' and not parsed_url.fragment and not parsed_url.query:
                truncated_url = truncated_url[:-1]
        if len(truncated_url) > max_length:
            truncated_url = truncated_url[:max_length] + '...'
        return truncated_url
    #
    # def get_alias_path(self):
    #     return reverse('url_shortener:alias', args=(self.alias,))
    #
    # def get_preview_path(self):
    #     return reverse('url_shortener:preview', args=(self.alias,))
