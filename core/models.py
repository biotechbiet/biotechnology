from django.db import models

# Create your models here.
class recruiter(models.Model):
    recruiter_name=models.CharField(max_length=100,help_text='recruiter name can be up to 100 characters')
    recruiter_pic=models.ImageField(upload_to='recruiters/',max_length=100 ,help_text='Please upload image in following types only GIF, JPG (or JPEG), PNG and BMP.')

class announcement(models.Model):
    date=models.DateField(help_text='Enter announcement date which is visible on News and announcement section')
    title=models.CharField(max_length=70)
    description=models.CharField(max_length=500)
