from django.shortcuts import render
from .models import publication
# Create your views here.
def publication_views(request):
    pub_object=publication.objects.all()
    return render(request,'publication/publication.html',{'publication_object':pub_object,'publication_active':'active'})
