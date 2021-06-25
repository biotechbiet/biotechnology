from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class product(models.Model):
    product_title=CharField(max_length=50)
    product_pic=ImageField(upload_to='product_image/')
    product_description=CharField(max_length=1000)
    
