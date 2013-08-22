#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import get_model

# Product = get_model('shop', 'Product')
# ProductType = get_model('configurableproduct', 'ProductType')


class ConfigurableProductBase(models.Model):

    """
    A configurable product class, has m2m relations to text, float and boolean fields
    """
    class Meta(object):
        abstract = True

    type = models.ForeignKey('ProductType', related_name="products", verbose_name=_('Type'), null=False, blank=False)
    char_fields = models.ManyToManyField('ProductCharField', through='ProductChar')
    float_fields = models.ManyToManyField('ProductFloatField', through='ProductFloat')
    boolean_fields = models.ManyToManyField('ProductBooleanField', through='ProductBoolean')
    image_fields = models.ManyToManyField('ProductImageField', through='ProductImage')
    file_fields = models.ManyToManyField('ProductFileField', through='ProductFile')

    product_fields = [
        ('char_fields', 'typechar_set'),
        ('float_fields', 'typefloat_set'),
        ('boolean_fields', 'typeboolean_set'),
        ('image_fields', 'typeimage_set'),
        ('file_fields', 'typefile_set')
    ]

    def save(self, *args, **kwargs):
        super(ConfigurableProductBase, self).save(*args, **kwargs)
        # Create relation for each field in product type
        for field_type in self.product_fields:
            self_field = getattr(self, field_type[0])
            type_field = getattr(self.type, field_type[1])
            for tf in type_field.all():
                if not self_field.through.objects.filter(field=tf.field, product=self).count():
                    pt = self_field.through(
                        product=self, field=tf.field, order=tf.order)
                    pt.save()

    @property
    def field_list(self):
        fields = list(self.productchar_set.all()) +\
                 list(self.productfloat_set.all()) +\
                 list(self.productboolean_set.all()) +\
                 list(self.productfile_set.all()) +\
                 list(self.productimage_set.all())
        fields.sort(key=lambda f: f.order)
        return fields

