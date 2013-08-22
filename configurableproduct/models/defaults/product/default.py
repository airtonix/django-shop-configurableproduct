#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.utils.translation import ugettext_lazy as _

from . import base


class Product(base.ConfigurableProductBase):

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        app_label = 'configurableproduct'