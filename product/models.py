from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class product(models.Model):
    product_title=CharField(max_length=50,help_text='title can be up to 50 letters and it is visible on products section')
    product_pic=ImageField(upload_to='product_image/',help_text='Images must be in following types GIF, JPG (or JPEG), PNG and BMP.')
    product_description=CharField(max_length=1000,help_text='description can be up to 1000 letters and it is visible on products section')
    
