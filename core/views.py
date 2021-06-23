from core.models import recruiter
from django.shortcuts import render
from .models import recruiter
# Create your views here.
def home_page(request):
    recruiter_objects=recruiter.objects.all()
    return render(request,'core/index.html',{'home_active':'active','recruiter_objects':recruiter_objects})
