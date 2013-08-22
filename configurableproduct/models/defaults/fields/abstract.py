#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _

from ...productmodel import Product
from ...producttypemodel import ProductType


class ProductAbstractField(models.Model):

    class Meta(object):
        abstract = True
        app_label = 'configurableproduct'

    name = models.CharField(max_length=200, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name


class BasicThroughField(models.Model):

    class Meta(object):
        abstract = True

    order = models.IntegerField(default=0, verbose_name=_('Ordering'))
    system = models.BooleanField(default=False, verbose_name=_('System'),
                                 help_text=_('Hide this field from customers?'))


class ProductAbstractFieldThrough(BasicThroughField):

    class Meta(object):
        abstract = True
        ordering = ['order']
        app_label = 'configurableproduct'

    product = models.ForeignKey(Product)


class TypeAbstractFieldThrough(BasicThroughField):

    class Meta(object):
        abstract = True
        ordering = ['order']
        app_label = 'configurableprodcut'

    type = models.ForeignKey(ProductType)
