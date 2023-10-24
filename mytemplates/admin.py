from django.contrib import admin
from .models import PreviewTemplate

# Register your models here.

class PreviewTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'templatePath')
    


admin.site.register(PreviewTemplate, PreviewTemplateAdmin)