from django.contrib import admin
from .models import recruiter
# Register your models here.
class RecruiterAdmin(admin.ModelAdmin):
    list_display=('recruiter_name','recruiter_pic')
admin.site.register(recruiter,RecruiterAdmin)
