#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.test import TestCase


CProduct = get_model('configurableproduct', 'CProduct')
ProductType = get_model('configurableproduct', 'ProductType')

ProductCharField = get_model('configurableproduct', 'ProductCharField')
ProductChar = get_model('configurableproduct', 'ProductChar')
TypeChar = get_model('configurableproduct', 'TypeChar')


class SimpleTest(TestCase):

    def setUp(self):
        self.pcf = ProductCharField(name='test char field')
        self.pcf.save()
        self.product_type = ProductType(name='test type')
        self.product_type.save()
        TypeChar.objects.create(field=self.pcf,
                                type=self.product_type,
                                order=2)

    def test_product_type(self):
        """
        Test for product type fields creation during product save
        """
        product = CProduct(type=self.product_type)
        product.save()
        self.assertEqual(product.productchar_set.all()[0].field, self.pcf)
        self.assertEqual(product.productchar_set.all()[0].order, 2)
