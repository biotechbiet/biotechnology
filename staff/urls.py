from django.urls import path
from . import views
urlpatterns = [
    path('teaching-staff/',views.teaching_staff_views,name='teaching_staff'),
    path('supporting-staff/',views.supporting_staff_views,name='supporting_staff'),
]
