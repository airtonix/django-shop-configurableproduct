#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'
__contributers__ = [
    'Zenobius Jiricek <airtonix@gmail.com>',
]

from django.contrib import admin
from django.conf import settings
from django.db.models import get_model

from sorl.thumbnail.admin.current import AdminImageWidget
from sorl.thumbnail.fields import ImageField


CProduct = get_model('configurableproduct', 'CProduct')
ProductType = get_model('configurableproduct', 'ProductType')

TypeChar = get_model('configurableproduct', 'TypeChar')
TypeBoolean = get_model('configurableproduct', 'TypeBoolean')
TypeFloat = get_model('configurableproduct', 'TypeFloat')
TypeImage = get_model('configurableproduct', 'TypeImage')
TypeFile = get_model('configurableproduct', 'TypeFile')

ProductChar = get_model('configurableproduct', 'ProductChar')
ProductBoolean = get_model('configurableproduct', 'ProductBoolean')
ProductFloat = get_model('configurableproduct', 'ProductFloat')
ProductImage = get_model('configurableproduct', 'ProductImage')
ProductFile = get_model('configurableproduct', 'ProductFile')

ProductCharField = get_model('configurableproduct', 'ProductCharField')
ProductBooleanField = get_model('configurableproduct', 'ProductBooleanField')
ProductFloatField = get_model('configurableproduct', 'ProductFloatField')
ProductImageField = get_model('configurableproduct', 'ProductImageField')
ProductFileField = get_model('configurableproduct', 'ProductFileField')


class AbstractTypeAdmin(admin.TabularInline):
    extra = 0
    can_delete = True
    fieldsets = [
        ['', {'fields': ['field', 'order', 'system']}]
    ]


class AbstractFieldInline(admin.TabularInline):
    extra = 0
    can_delete = True
    fieldsets = [
        ['', {'fields': ['field', 'value', 'order', 'system']}]
    ]


class ProductCharInline(AbstractFieldInline):
    model = ProductChar


class ProductBooleanInline(AbstractFieldInline):
    model = ProductBoolean


class ProductFloatInline(AbstractFieldInline):
    model = ProductFloat


class ProductImageInline(AbstractFieldInline):
    model = ProductImage
    # formfield_overrides = {
    #     ImageField: {'widget': AdminImageWidget}
    # }
    fieldsets = [
        ['', {'fields': ['field', 'value', 'order', 'system', 'is_primary']}]
    ]


class ProductFileInline(AbstractFieldInline):
    model = ProductFile
    fieldsets = [
        ['', {'fields': ['field', 'value', 'order', 'system', 'is_commodity']}]
    ]


class TypeCharAdmin(AbstractTypeAdmin):
    model = TypeChar


class TypeBooleanAdmin(AbstractTypeAdmin):
    model = TypeBoolean


class TypeFloatAdmin(AbstractTypeAdmin):
    model = TypeFloat


class TypeImageAdmin(AbstractTypeAdmin):
    model = TypeImage


class TypeFileAdmin(AbstractTypeAdmin):
    model = TypeFile


class ProductTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {'fields': ['name', ]}),
    )
    list_per_page = 100
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [TypeCharAdmin,
               TypeBooleanAdmin,
               TypeFloatAdmin,
               TypeImageAdmin,
               TypeFileAdmin
               ]


class CProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {'fields': ['type', 'unit_price', 'name', 'slug', 'active']}),
    )
    prepopulated_fields = {'slug': ['name']}
    inlines = [ProductCharInline,
               ProductBooleanInline,
               ProductFloatInline,
               ProductImageInline,
               ProductFileInline
               ]


admin.site.register(ProductCharField)
admin.site.register(ProductBooleanField)
admin.site.register(ProductFloatField)
admin.site.register(ProductImageField)
admin.site.register(ProductFileField)
admin.site.register(ProductType, ProductTypeAdmin)
if getattr(settings, 'ENABLE_CPRODUCT_ADMIN', False):
    admin.site.register(CProduct, CProductAdmin)
