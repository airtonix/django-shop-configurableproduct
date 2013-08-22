====================================
Configurable product for Django-shop
====================================

This plugin allow you to:

* Define product types in django admin interface with custom set of fields
* Add custom fields to products

Supported field types
=====================

* Float field
* Char field
* Image field
  - is_primary
* File field
  - is_commodity
* Boolean field (NullBooleanField)

Additionally each field type sports a 'system' attribute field to signify that an instance
of a field shouldn't be presented to customers.


How to use it
=============

* Install from github
* Play with the example project
* If you want to use ConfigurableProduct model directly, set `ENABLE_CPRODUCT_ADMIN` to `True` in your settings file.
* You can access custom fields via `productfloat_set`, `productchar_set`,... as::

   product_object.productchar_set.all()[0].value

  * `*_set.get_query_set()` methods on fields won't return fields marked as `system`
  * `*_set.system()` methods on fields only returns fields marked as `system`
  * image fields expose a special queryset ::

       > image = product_object.productimage_set.primary()
       > print image.value
         "/files/insert-proper-uuid-here.gif.png.mp4.avi"

* You can access ordered list of custom fields via `product_object.field_list` property

