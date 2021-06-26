from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class teaching_staff(models.Model):
    name=CharField(max_length=70,help_text='name can be up to 100 letters')
    profile_pic=ImageField(upload_to='teaching_staff/',max_length=70,help_text='pic must be in following types GIF, JPG (or JPEG), PNG and BMP.')
    designation=CharField(max_length=70,help_text='designation can be up to 70 letters')
    qualification=CharField(max_length=70,help_text='Write all qualification seprated by comma and it can be up to 70 letters')
    area_of_interest=CharField(max_length=70,help_text='it can be up to 70 letters')


class supporting_staff(models.Model):
    name=CharField(max_length=70,help_text='name can be up to 70 letters')
    profile_pic=ImageField(upload_to='supporting_staff/',max_length=70,help_text='pic must be in following types GIF, JPG (or JPEG), PNG and BMP.')
    designation=CharField(max_length=70,help_text='designation can be up to 70 letters')
    qualification=CharField(max_length=70,help_text='Write all qualification seprated by comma and it can be up to 70 letters')
    area_of_interest=CharField(max_length=70,help_text='it can be up to 70 letters')