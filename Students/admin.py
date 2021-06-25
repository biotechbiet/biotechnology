from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import topper_list,project_list,placement_list,eNews_magazine

class TopperAdmin(admin.ModelAdmin):
    list_display=('stu_rank','stu_name','stu_percentage','stu_year','session')
admin.site.register(topper_list,TopperAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display=('session','file')
admin.site.register(project_list,ProjectAdmin)

class PlacementAdmin(admin.ModelAdmin):
    list_display=('stu_name','company_name','session')
admin.site.register(placement_list,PlacementAdmin)

class Enews_magazineAdmin(admin.ModelAdmin):
    list_display=('title','session','file')

admin.site.register(eNews_magazine,Enews_magazineAdmin)