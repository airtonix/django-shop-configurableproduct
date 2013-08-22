#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _


class ConfigurableProductTypeBase(models.Model):

    class Meta(object):
        abstract = True

    name = models.CharField(max_length=200, verbose_name=_('Name'), blank=False, unique=True)
    char_fields = models.ManyToManyField('ProductCharField', verbose_name=_('Char field'), blank=True, null=True, through='TypeChar')
    float_fields = models.ManyToManyField('ProductFloatField', verbose_name=_('Float field'), blank=True, null=True, through='TypeFloat')
    boolean_fields = models.ManyToManyField('ProductBooleanField', verbose_name=_('Boolean field'), blank=True, null=True, through='TypeBoolean')
    image_fields = models.ManyToManyField('ProductImageField', verbose_name=_('Image field'), blank=True, null=True, through='TypeImage')
    file_fields = models.ManyToManyField('ProductFileField', verbose_name=_('File field'), blank=True, null=True, through='TypeFile')

    def __unicode__(self):
        return self.name
