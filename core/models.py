from django.db import models

# Create your models here.
class recruiter(models.Model):
    recruiter_name=models.CharField(max_length=100)
    recruiter_pic=models.ImageField(upload_to='recruiters/',max_length=100)

class announcement(models.Model):
    date=models.DateField()
    title=models.CharField(max_length=70)
    description=models.CharField(max_length=500)