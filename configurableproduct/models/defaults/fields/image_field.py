#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

import uuid
import os

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from sorl.thumbnail import ImageField, get_thumbnail
from sorl.thumbnail.helpers import ThumbnailError

from . import abstract


UPLOAD_PATH = getattr(settings, 'PRODUCT_IMAGE_UPLOAD_TO', "products/{product_id}/images/{file_uuid}{file_ext}")


class ProductImageField(abstract.ProductAbstractField):

    class Meta(object):
        verbose_name = _('Product field - image')
        verbose_name_plural = _('Product fields - image')
        app_label = 'configurableproduct'


class ProductImageManager(models.Manager):

    def primary(self):
        return self.get_queryset().filter(is_primary=True)


class ProductImage(abstract.ProductAbstractFieldThrough):

    class Meta(abstract.ProductAbstractFieldThrough.Meta):
        verbose_name = _('Product image field')
        verbose_name_plural = _('Product image field')
        app_label = 'configurableproduct'

    def get_file_path(instance, filename):
        filename, file_ext = os.path.splitext(filename)
        file_uuid = uuid.uuid4()
        kwargs = {
            "product_id": instance.product.id,
            "file_uuid": file_uuid,
            "file_ext": file_ext,
            "filename": filename,
        }
        return UPLOAD_PATH.format(**kwargs)

    def admin_thumbnail(self):
        try:
            return '<img src="%s">' % get_thumbnail(self.value, '100x100', crop='center').url
        except IOError:
            return 'IOError'
        except ThumbnailError as ex:
            return 'ThumbnailError, %s' % ex.message

    admin_thumbnail.short_description = _('Thumbnail')
    admin_thumbnail.allow_tags = True

    description = models.CharField(
        max_length=200, verbose_name=_('Description'), blank=True, null=True)
    value = ImageField(verbose_name=_('File'), upload_to=get_file_path)
    field = models.ForeignKey('ProductImageField', verbose_name=_('Field'))
    is_primary = models.BooleanField(default=False)

    objects = ProductImageManager()


class TypeImage(abstract.TypeAbstractFieldThrough):

    class Meta(abstract.TypeAbstractFieldThrough.Meta):
        verbose_name = _('Image field')
        verbose_name_plural = _('Image fields')
        app_label = 'configurableproduct'

    field = models.ForeignKey('ProductImageField', verbose_name=_('Field'))
