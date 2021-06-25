from django.contrib import admin

# Register your models here.
from . models import product

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_title','product_pic','product_description')

admin.site.register(product,ProductAdmin)