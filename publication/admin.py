from django.contrib import admin
from .models import publication
# Register your models here.
class publicationAdmin(admin.ModelAdmin):
    list_display=('publication_file',)

admin.site.register(publication,publicationAdmin)