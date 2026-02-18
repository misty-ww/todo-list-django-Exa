from django.contrib import admin
from .models import Task,Category

@admin.register(Task)
class tasksAdmin(admin.ModelAdmin):
    list_display=['name','description','status','date','category']
    list_editable = ['description','status','category']
    
@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display=['name',]