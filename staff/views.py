from django.shortcuts import render
from .models import teaching_staff,supporting_staff
# Create your views here.
def teaching_staff_views(request):
    teaching_staff_list=teaching_staff.objects.all()
    return render(request,'staff/teaching_staff.html',{'teaching_staff':teaching_staff_list,'staff_active':'active'})

def supporting_staff_views(request):
    supporting_staff_list=supporting_staff.objects.all()
    return render(request,'staff/supporting_staff.html',{'supporting_staff':supporting_staff_list,'staff_active':'active'})
