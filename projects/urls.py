from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.ProjectListView.as_view(),name='Project_list'),

    path('project/create',views.ProjectCreatView.as_view(),name='Project_create'),
    
    path('project/edit/<int:pk>',views.ProjectUpdateView.as_view(),name='Project_update'),
    path('task/create',views.TaskCreateView.as_view(),name='Task_create'),
    path('task/delete/<int:pk>',views.TaskDeleteViews.as_view(),name='Task_delete')

]


