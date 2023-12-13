from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

# Register your models here.
from . import models
admin.site.register(models.Category)

@admin.register(models.Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title','status','user','category','created_at']
    list_per_page=20
    list_select_related=['category','user']
    list_editable=['status']
    
    def tasks_count(self,obj):
        # return obj.task_set.count()
        return obj.tasks_count
    
    def get_queryset(self, request):
        query=super().get_queryset(request)
        
        return query


# admin.site.register(models.Task)

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    list_display=['id','description','project','is_completed']
    list_editable=['is_completed']
    list_per_page=20