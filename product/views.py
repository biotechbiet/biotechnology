from django.shortcuts import render
from .models import product
# Create your views here.
def product_views(request):
    product_objects=reversed(product.objects.all())
    return render(request,'product/product.html',{'products_active':'active','product_objects':product_objects})
