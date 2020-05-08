# -*- coding: utf-8 -*-

import string

from django.conf import settings
from hashids import Hashids

from apps.contrib.api.exceptions import SimpleValidationError
from apps.shortener.models import Link
from apps.shortener.response_codes import LINK_ALIAS_IS_ALREADY_USED


class LinkService(object):

    @classmethod
    def make_encoder(cls):
        return Hashids(salt=settings.DJANGO_SECRET_KEY, alphabet=string.ascii_lowercase)

    @classmethod
    def generate_alias(cls):
        latest_link = Link.objects.latest('id')
        enconder = cls.make_encoder()
        return enconder.encode(latest_link.id)

    @classmethod
    def create_link(cls, url, alias=None, owner=None):
        if Link.objects.filter(alias=alias).exists():
            raise SimpleValidationError(**LINK_ALIAS_IS_ALREADY_USED)

        _alias = alias or cls.generate_alias()
        return Link.objects.create(url=url, alias=_alias, owner=owner)
