#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _


from .abstract import ProductAbstractField, ProductAbstractFieldThrough, TypeAbstractFieldThrough


class ProductCharField(ProductAbstractField):

    class Meta(object):
        verbose_name = _('Product field - char')
        verbose_name_plural = _('Product fields - char')
        app_label = 'configurableproduct'


class ProductChar(ProductAbstractFieldThrough):

    class Meta(ProductAbstractFieldThrough.Meta):
        verbose_name = _('Char field')
        verbose_name_plural = _('Char fields')
        app_label = 'configurableproduct'

    value = models.CharField(max_length=200,
        verbose_name=_('Value'), default=None, null=True, blank=True)
    field = models.ForeignKey('ProductCharField', verbose_name=_('Field'))


class TypeChar(TypeAbstractFieldThrough):

    class Meta(TypeAbstractFieldThrough.Meta):
        verbose_name = _('Char field')
        verbose_name_plural = _('Char fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey('ProductCharField', verbose_name=_('Field'))
