#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.utils.translation import ugettext_lazy as _

from shop.models_bases import BaseProduct
from shop.models_bases.managers import (
    ProductManager,
    ProductStatisticsManager,
)

from . import base


class Product(base.ConfigurableProductBase, BaseProduct):
    objects = ProductManager()
    statistics = ProductStatisticsManager()

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        app_label = 'configurableproduct'