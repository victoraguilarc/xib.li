# -*- coding: utf-8 -*-

from django.urls import path, include

from apps.shortener.views.home import HomeView
from apps.shortener.views.link import LinkView
from apps.shortener.views.profile import ProfileView

app_name = 'shortener'
urlpatterns = [
    path(
        'dash/',
        HomeView.as_view(),
        name='confirm-email',
    ),
    path(
        'profile/',
        view=ProfileView.as_view(),
        name='profile',
    ),

    path(
        'link/<slug:uuid>/',
        view=LinkView.as_view(),
        name='link-detail',
    )
]
