# -*- coding: utf-8 -*-

from django.urls import path, include

app_name = 'shortener'
urlpatterns = [
    path('v1/', include('apps.shortener.api.v1.urls', namespace='v1')),
]
