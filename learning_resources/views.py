from django.shortcuts import render
from .models import video,usefull_link,usefull_format,question_paper
# Create your views here.
def video_views(request):
    video_objects=reversed(video.objects.all())
    return render(request,'learning_resources/video.html',{'learning_resources_active':'active','video_objects':video_objects})

def usefull_format_views(request):
    usefull_format_objects=reversed(usefull_format.objects.all())
    return render(request,'learning_resources/usefull_format.html',{'learning_resources_active':'active','usefull_format_objects':usefull_format_objects})
def usefull_link_views(request):
    usefull_link_objects=reversed(usefull_link.objects.all())
    return render(request,'learning_resources/usefull_link.html',{'learning_resources_active':'active','usefull_link_objects':usefull_link_objects})
def question_paper_views(request):
    question_paper_objects=reversed(question_paper.objects.all())
    return render(request,'learning_resources/question_paper.html',{'learning_resources_active':'active','question_paper_objects':question_paper_objects})
