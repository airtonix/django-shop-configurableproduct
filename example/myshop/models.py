from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from polymorphic.manager import PolymorphicManager
from shop.util.loader import load_class
from configurableproduct.models import *


Product = load_class(
    'configurableproduct.models.defaults.product.default.Product')
ProductType = load_class(
    'configurableproduct.models.defaults.producttype.default.ProductType')
ProductChar = load_class(
    'configurableproduct.models.defaults.fields.char_field.ProductChar')


class Product(Product):

    class Meta:
        app_label = "digitalshop"
        abstract = False
