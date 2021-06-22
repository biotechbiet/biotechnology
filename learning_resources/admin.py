from django.contrib import admin

# Register your models here.
from .models import video,usefull_link,usefull_format,question_paper
class VideoAdmin(admin.ModelAdmin):
    list_display=('video_title','video_url',)
admin.site.register(video,VideoAdmin)

class Usefull_linkAdmin(admin.ModelAdmin):
    list_display=('link_title','link_url',)
admin.site.register(usefull_link,Usefull_linkAdmin)

class Usefull_formatAdmin(admin.ModelAdmin):
    list_display=('format_title','format_file',)
admin.site.register(usefull_format,Usefull_formatAdmin)

class Question_paperAdmin(admin.ModelAdmin):
    list_display=('question_paper_title','question_paper_file',)
admin.site.register(question_paper,Question_paperAdmin)