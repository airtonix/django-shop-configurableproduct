from django.conf import settings
from shop.util.loader import load_class


PRODUCT_TYPE_MODEL = getattr(settings, 'SHOP_PRODUCT_TYPE_MODEL',
    'configurableproduct.models.defaults.producttype.default.ProductType')
ProductType = load_class(PRODUCT_TYPE_MODEL, 'SHOP_PRODUCT_TYPE_MODEL')
