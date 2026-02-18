from django.contrib import admin
from .models import tasks

@admin.register(tasks)
class tasksAdmin(admin.ModelAdmin):
    list_display=['name','description','status','date','category']
    list_editable = ['description','status','category']
    