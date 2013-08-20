#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

import os
import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import abstract


# noinspection PyUnusedLocal
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(getattr(settings, 'PRODUCT_FILE_UPLOAD_TO', os.path.join('products', 'files')), filename)


class ProductFileField(abstract.ProductAbstractField):

    class Meta(object):
        verbose_name = _('Product field - file')
        verbose_name_plural = _('Product fields - file')
        app_label = 'configurableproduct'


class ProductFile(abstract.ProductAbstractFieldThrough):

    class Meta(abstract.ProductAbstractFieldThrough.Meta):
        verbose_name = _('Product file field')
        verbose_name_plural = _('Product file field')
        app_label = 'configurableproduct'

    description = models.CharField(
        max_length=200, verbose_name=_('Description'), blank=True, null=True)
    value = models.FileField(verbose_name=_('File'), upload_to=get_file_path)
    field = models.ForeignKey('ProductFileField', verbose_name=_('Field'))


class TypeFile(abstract.TypeAbstractFieldThrough):

    class Meta(abstract.TypeAbstractFieldThrough.Meta):
        verbose_name = _('File field')
        verbose_name_plural = _('File fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey('ProductFileField', verbose_name=_('Field'))
