from django.db import models

# Create your models here.
class recruiter(models.Model):
    recruiter_name=models.CharField(max_length=100,help_text='recruiter name can be up to 100 letters')
    recruiter_pic=models.ImageField(upload_to='recruiters/',max_length=100 ,help_text='Images must be in following types GIF, JPG (or JPEG), PNG and BMP.')

class announcement(models.Model):
    date=models.DateField(help_text='This announcement date will visible on News and announcement section')
    title=models.CharField(max_length=70,help_text='title can be up to 70 letters')
    description=models.CharField(max_length=500,help_text='description can be up to 500 letters and it will visible on News and announcement section')
