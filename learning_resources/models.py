from django.db import models

# Create your models here.
class video(models.Model):
    video_title=models.CharField(max_length=200)
    video_url=models.CharField(max_length=500)

class usefull_link(models.Model):
    link_title=models.CharField(max_length=200)
    link_url=models.CharField(max_length=500)

class usefull_format(models.Model):
    format_title=models.CharField(max_length=200)
    format_file=models.FileField(upload_to='usefull_format/',max_length=200)

class question_paper(models.Model):
    question_paper_title=models.CharField(max_length=200)
    question_paper_file=models.FileField(upload_to='question_paper/',max_length=200)
