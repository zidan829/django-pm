from django.shortcuts import render
from django.views.generic import ListView,CreateView
from . import models 
from . import forms
from django.urls import reverse_lazy
# Create your views here.

class ProjectListView(ListView):
    model=models.Projects
    template_name='project/list.html'

class ProjectCreatView(CreateView):
    model=models.Projects
    form_class=forms.ProjectCreateForm
    template_name='project/creat.html'
    success_url=reverse_lazy('Project_list')
