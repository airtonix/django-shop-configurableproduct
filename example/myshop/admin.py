from django.contrib import admin

from configurableproduct.admin import *
from . import models


admin.site.register(models.Product, CProductAdmin)
