from django.urls import path
from . import views
urlpatterns = [
    path('videos/',views.video_views,name='video_url'),
    path('usefull-formats/',views.usefull_format_views,name='usefull_format_url'),
    path('usefull-links/',views.usefull_link_views,name='usefull_link_url'),
    path('question-paper/',views.question_paper_views,name='question_paper_url'),
]
