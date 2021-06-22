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
        ('Forth Year','Forth Year'),
    )
    stu_rank=CharField(max_length=3,choices=rank_choice)
    stu_name=CharField(max_length=70)
    stu_percentage=FloatField()
    stu_year=CharField(max_length=15,choices=year_choice)
    session=CharField(max_length=9)

class project_list(models.Model):
    session = CharField(max_length=9)
    file = FileField(upload_to='project_file/')

class placement_list(models.Model):
    stu_name=CharField(max_length=70)
    company_name=CharField(max_length=120)
    session=CharField(max_length=9)
