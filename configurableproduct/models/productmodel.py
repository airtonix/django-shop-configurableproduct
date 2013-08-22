from django.conf import settings
from shop.util.loader import load_class


PRODUCT_MODEL = getattr(settings, 'SHOP_PRODUCT_MODEL',
    'configurableproduct.models.defaults.product.default.Product')
Product = load_class(PRODUCT_MODEL, 'SHOP_PRODUCT_MODEL')

