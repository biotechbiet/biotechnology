from django.contrib import admin
from .models import recruiter,announcement
# Register your models here.
class RecruiterAdmin(admin.ModelAdmin):
    list_display=('recruiter_name','recruiter_pic')
admin.site.register(recruiter,RecruiterAdmin)

class announcementAdmin(admin.ModelAdmin):
    list_display=('date','title','description')
admin.site.register(announcement,announcementAdmin)