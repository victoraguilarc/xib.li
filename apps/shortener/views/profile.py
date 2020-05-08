# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'shotener/profile.html'

    def get(self, request, **kwargs):
        """It renders the html template to confirm email."""
        return super().get(request, **kwargs)
