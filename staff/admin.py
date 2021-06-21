from staff.models import teaching_staff
from django.contrib import admin
from .models import teaching_staff,supporting_staff
# Register your models here.

class TeachingAdmin(admin.ModelAdmin):
    list_display=('name','profile_pic','designation','qualification','area_of_interest')

admin.site.register(teaching_staff,TeachingAdmin)

class SupportingAdmin(admin.ModelAdmin):
    list_display=('name','profile_pic','designation','qualification','area_of_interest')

admin.site.register(supporting_staff,SupportingAdmin)