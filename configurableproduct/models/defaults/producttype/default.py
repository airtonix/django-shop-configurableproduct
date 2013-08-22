#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.utils.translation import ugettext_lazy as _

from . import base


class ProductType(base.ConfigurableProductTypeBase):

    class Meta:
        verbose_name = _('Product type')
        verbose_name_plural = _('Product types')
        app_label = 'configurableproduct'
