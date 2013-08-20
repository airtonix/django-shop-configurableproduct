#!/usr/bin/env python
# vim:fileencoding=utf-8

__author__ = 'zeus'

from django.contrib import admin
from django.conf import settings

from sorl.thumbnail.admin.current import AdminImageWidget
from sorl.thumbnail.fields import ImageField

from .models.product import CProduct, ProductType
from .models.fields import char_field, boolean_field, float_field, image_field, file_field


class AbstractTypeAdmin(admin.TabularInline):
    extra = 0
    can_delete = True
    fieldsets = [
        ['', {'fields': ['field', 'order']}]
    ]


class AbstractFieldInline(admin.TabularInline):
    extra = 0
    can_delete = True
    fieldsets = [
        ['', {'fields': ['field', 'value', 'order']}]
    ]


class ProductCharInline(AbstractFieldInline):
    model = char_field.ProductChar


class ProductBooleanInline(AbstractFieldInline):
    model = boolean_field.ProductBoolean


class ProductFloatInline(AbstractFieldInline):
    model = float_field.ProductFloat


class ProductImageInline(AbstractFieldInline):
    model = image_field.ProductImage
    formfield_overrides = {
        ImageField: {'widget': AdminImageWidget}
    }


class ProductFileInline(AbstractFieldInline):
    model = file_field.ProductFile


class TypeCharAdmin(AbstractTypeAdmin):
    model = char_field.TypeChar


class TypeBooleanAdmin(AbstractTypeAdmin):
    model = boolean_field.TypeBoolean


class TypeFloatAdmin(AbstractTypeAdmin):
    model = float_field.TypeFloat


class TypeImageAdmin(AbstractTypeAdmin):
    model = TypeImage


class TypeFileAdmin(AbstractTypeAdmin):
    model = TypeFile


class ProductTypeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {'fields': ['name']}),
    )
    list_per_page = 100
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [TypeCharAdmin, TypeBooleanAdmin,
               TypeFloatAdmin, TypeImageAdmin, TypeFileAdmin]


class CProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('', {'fields': ['type', 'unit_price', 'name', 'slug', 'active']}),
    )
    inlines = [ProductCharInline, ProductBooleanInline,
               ProductFloatInline, ProductImageInline, ProductFileInline]
    prepopulated_fields = {'slug': ['name']}


admin.site.register(char_field.ProductCharField)
admin.site.register(boolean_field.ProductBooleanField)
admin.site.register(float_field.ProductFloatField)
admin.site.register(image_field.ProductImageField)
admin.site.register(file_field.ProductFileField)
admin.site.register(ProductType, ProductTypeAdmin)
if getattr(settings, 'ENABLE_CPRODUCT_ADMIN', False):
    admin.site.register(CProduct, CProductAdmin)
