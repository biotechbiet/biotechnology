from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('topper-list/',views.toppers_list,name='topper_list'),
    path('project-list/',views.projects_list,name='project_list'),
    path('placements/',views.placements_list,name='placement_list'),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)