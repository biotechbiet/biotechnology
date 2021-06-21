from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class teaching_staff(models.Model):
    name=CharField(max_length=70)
    profile_pic=ImageField(upload_to='teaching_staff/',max_length=70)
    designation=CharField(max_length=70)
    qualification=CharField(max_length=70)
    area_of_interest=CharField(max_length=70)


class supporting_staff(models.Model):
    name=CharField(max_length=70)
    profile_pic=ImageField(upload_to='supporting_staff/',max_length=70)
    designation=CharField(max_length=70)
    qualification=CharField(max_length=70)
    area_of_interest=CharField(max_length=70)