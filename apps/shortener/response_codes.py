# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


LINK_ALIAS_IS_ALREADY_USED = {
    'code': 'links.AliasIsAlreadyUsed',
    'detail': _('The link alias is already used.'),
}
LINK_NOT_FOUND = {
    'code': 'links.NotFound',
    'detail': _('Redirection Link not found.'),
}
