from django.shortcuts import render
from .models import topper_list,project_list,placement_list,eNews_magazine
# Create your views here.
def toppers_list(request):
    top_list=topper_list.objects.all()
    topper={}
    all_sessions=set()
    for i in top_list:
        all_sessions.add(i.session)
    all_sessions=list(all_sessions)
    all_sessions.sort(reverse=True)
    for i in all_sessions:
        topper[i]=topper_list.objects.all().filter(session=i)
    return render(request,'Students/topper_list.html',{'toppers':topper,'students_active':'active'})

def projects_list(request):
    pro_list=reversed(project_list.objects.all())
    return render(request,'Students/project_list.html',{'project_list':pro_list,'students_active':'active'})
    
def placements_list(request):
    place_list=placement_list.objects.all()
    all_sessions=set()
    for i in place_list:
        all_sessions.add(i.session)
    all_sessions=list(all_sessions)
    all_sessions.sort(reverse=True)
    placements={}
    for i in all_sessions:
        placements[i]=placement_list.objects.all().filter(session=i)
    return render(request,'Students/placement_list.html',{'placement_list':placements,'students_active':'active'})

def enews_magazine_views(request):
    eNews_magazine_objects=eNews_magazine.objects.all()
    all_objects=set()
    for i in eNews_magazine_objects:
        all_objects.add(i.session)
    all_objects=list(all_objects)
    all_objects.sort(reverse=True)
    eNews_magazine_context={}
    for i in all_objects:
        eNews_magazine_context[i]=eNews_magazine.objects.filter(session=i)
    return render(request,'Students/eNews_magazine.html',{'eNews_magazine_active':'active','eNews_magazine_objects':eNews_magazine_context})