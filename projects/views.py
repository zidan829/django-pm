from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models 
from . import forms
from django.urls import reverse_lazy,reverse
# Create your views here.

class ProjectListView(ListView):
    model=models.Projects
    template_name='project/list.html'

class ProjectCreatView(CreateView):
    model=models.Projects
    form_class=forms.ProjectCreateForm
    template_name='project/creat.html'
    success_url=reverse_lazy('Project_list')

class ProjectUpdateView(UpdateView):
    model=models.Projects
    form_class=forms.ProjectUpdateForm
    template_name='project/update.html'

    def get_success_url(self):
        return reverse('Project_update',args=[self.object.id])

class TaskCreateView(CreateView):
    model=models.Task
    fields=['project','description']
    
    
    def get_success_url(self):
        return reverse('Project_update',args=[self.object.project.id])
    

class TaskUpdateView(UpdateView):
    model=models.Task
    fields=['project','description']
    http_method_names=['is_completed']
    def get_success_url(self):
        return reverse('Project_update',args=[self.object.project.id])
    
class TaskDeleteViews(DeleteView):
    model=models.Task
    def get_success_url(self):
        return reverse('Project_update',args=[self.object.id])

