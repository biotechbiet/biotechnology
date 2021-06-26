from django.db import models

# Create your models here.
class publication(models.Model):
    publication_file=models.FileField(max_length=100,help_text='file must be in pdf format')
