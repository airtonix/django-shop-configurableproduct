#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import abstract


class ProductFloatField(abstract.ProductAbstractField):

    class Meta(object):
        verbose_name = _('Product field - float')
        verbose_name_plural = _('Product fields - float')
        app_label = 'configurableproduct'


class ProductFloat(abstract.ProductAbstractFieldThrough):

    class Meta(abstract.ProductAbstractFieldThrough.Meta):
        verbose_name = _('Float field')
        verbose_name_plural = _('Float fields')
        app_label = 'configurableproduct'

    value = models.FloatField(
        verbose_name=_('Value'), default=None, null=True, blank=True)
    field = models.ForeignKey('ProductFloatField', verbose_name=_('Field'))


class TypeFloat(abstract.TypeAbstractFieldThrough):

    class Meta(abstract.TypeAbstractFieldThrough.Meta):
        verbose_name = _('Float field')
        verbose_name_plural = _('Float fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey('ProductFloatField', verbose_name=_('Field'))
