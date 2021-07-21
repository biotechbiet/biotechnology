from django.db import models
from django.db.models.fields import CharField, FloatField
from django.db.models.fields.files import FileField

# Create your models here.
class topper_list(models.Model):
    rank_choice = (
        ('1st', '1st'),
        ('2nd', '2nd'),
        ('3rd', '3rd'),
    )
    year_choice=(
        ('First Year','First Year'),
        ('Second Year','Second Year'),
        ('Third Year','Third Year'),
        ('Fourth Year','Fourth Year'),
    )
    stu_rank=CharField(max_length=3,choices=rank_choice,help_text='it is visible on webpage')
    stu_name=CharField(max_length=70,help_text='name can be up to 70 letters')
    stu_percentage=FloatField(help_text='it is visible on webpage')
    stu_year=CharField(max_length=15,choices=year_choice,help_text='it is visible on webpage')
    session=CharField(max_length=9,help_text='session must be in yyyy-yyyy format .example: 2021-2022')

class project_list(models.Model):
    session = CharField(max_length=9,help_text='session must be in yyyy-yyyy format .example: 2021-2022')
    file = FileField(upload_to='project_file/',help_text='it can be in any document type file')

class placement_list(models.Model):
    stu_name=CharField(max_length=70,help_text='name can be up to 70 letters')
    company_name=CharField(max_length=120,help_text='name can be up to 120 letters')
    session=CharField(max_length=9,help_text='session must be in yyyy-yyyy format .example: 2021-2022')

class eNews_magazine(models.Model):
    title=CharField(max_length=500,help_text='title can be up to 500 letters')
    session=CharField(max_length=9,help_text='session must be in yyyy-yyyy format .example: 2021-2022')
    file=FileField(upload_to='eNews_Magazine/',help_text='it can be in any document type file')
