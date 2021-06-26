from django.db import models

# Create your models here.
class video(models.Model):
    video_title=models.CharField(max_length=200,help_text='video title can be up to 200 letters and it is visible on video section')
    video_url=models.CharField(max_length=500,help_text='video url can be up to 500 Characters')

class usefull_link(models.Model):
    link_title=models.CharField(max_length=200,help_text='title can be up to 200 letters and it is visible on video section')
    link_url=models.CharField(max_length=500,help_text='url can be up to 500 Characters')

class usefull_format(models.Model):
    h='title can be up to 200 letters and it is visible on usefull format section'
    format_title=models.CharField(max_length=200 ,help_text=h)
    format_file=models.FileField(upload_to='usefull_format/',max_length=200,help_text='File can be in any format and file name can be up to 200 characters')

class question_paper(models.Model):
    h='title can be up to 200 letters and it is visible on question paper section'
    question_paper_title=models.CharField(max_length=200,help_text=h)
    h='File can be in any format and file name can be up to 200 characters'
    question_paper_file=models.FileField(upload_to='question_paper/',max_length=200,help_text=h)
