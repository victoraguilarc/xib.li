# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'shotener/home.html'

    def get(self, request, **kwargs):
        """It renders the html template to confirm email."""
        return super().get(request, **kwargs)
