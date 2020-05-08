from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound

from apps.shortener.models import Link
from apps.shortener.response_codes import LINK_NOT_FOUND


class LinkSelector(object):

    @classmethod
    def get_or_404(cls, alias):
        link = get_object_or_404(Link, alias__iexact=alias)
        link.clicks_count += 1
        link.save()
        return link

    @classmethod
    def get_by_alias(cls, alias):
        try:
            return Link.objects.get(alias=alias)
        except Link.DoesNotExist:
            raise NotFound(**LINK_NOT_FOUND)
