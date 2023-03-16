from django.contrib import admin

from products.models import Product, Version

#  123@123.ru
#  123
admin.site.register(Product)
admin.site.register(Version)
