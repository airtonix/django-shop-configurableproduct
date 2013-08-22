#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

import os
import uuid

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string

from . import abstract


LICENSE_KEY_GENERATOR = getattr(settings, "LICENSE_KEY_GENERATOR", lambda instance, order: get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'))
UPLOAD_PATH = getattr(settings, 'PRODUCT_FILE_UPLOAD_TO', "products/{product_id}/files/{file_uuid}.{file_ext}")

# noinspection PyUnusedLocal


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

    def get_file_path(instance, filename):
        filename, file_ext = filename.splitext()
        file_uuid = uuid.uuid4()
        kwargs = {
            "product_id": instance.product.id,
            "file_uuid": file_uuid,
            "file_ext": file_ext,
            "filename": filename,
        }
        return UPLOAD_PATH.format(**kwargs)

        if instance.is_commodity:
            return os.path.join(getattr(settings, 'PRODUCT_PROTECTED_FILE_UPLOAD_TO',
                os.path.join('products', instance.product.type, instance.product.slug)), filename)

        else:
            return os.path.join(getattr(settings, 'PRODUCT_PUBLIC_FILE_UPLOAD_TO',
                os.path.join('products', instance.product.type, instance.product.slug)), filename)

    def generate_license_key(self, order):
        if self.requires_license_key and LICENSE_KEY_GENERATOR is not None:
            return LICENSE_KEY_GENERATOR(self, order)
        return None

    is_commodity = models.BooleanField(
        default=False, verbose_name=_('Commodity'),
        help_text=_('Is the file part of the purchased product, does it require payment to access?'))
    requires_license_key = models.BooleanField(
        default=False, verbose_name=_('Requires License Key'),
        help_text=_('Will this file require an unique key to unlock?'))
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
