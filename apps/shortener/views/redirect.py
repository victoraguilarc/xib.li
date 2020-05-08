# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponsePermanentRedirect

from apps.shortener.selectors.link_selector import LinkSelector


class RedirectView(View):

    def get(self, request, alias, **kwargs):
        link = LinkSelector.get_or_404(alias)
        return HttpResponsePermanentRedirect(link.url)
