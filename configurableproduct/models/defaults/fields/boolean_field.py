#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import abstract


class ProductBooleanField(abstract.ProductAbstractField):

    class Meta(object):
        verbose_name = _('Product field - boolean')
        verbose_name_plural = _('Product fields - boolean')
        app_label = 'configurableproduct'


class ProductBoolean(abstract.ProductAbstractFieldThrough):

    class Meta(abstract.ProductAbstractFieldThrough.Meta):
        verbose_name = _('Boolean field')
        verbose_name_plural = _('Boolean fields')
        app_label = 'configurableproduct'

    value = models.NullBooleanField(verbose_name=_('Value'), default=None, null=True, blank=True)
    field = models.ForeignKey('ProductBooleanField', verbose_name=_('Field'))


class TypeBoolean(abstract.TypeAbstractFieldThrough):

    class Meta(abstract.TypeAbstractFieldThrough.Meta):
        verbose_name = _('Boolean field')
        verbose_name_plural = _('Boolean fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey('ProductBooleanField', verbose_name=_('Field'))
