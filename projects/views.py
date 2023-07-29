from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Project, Task
from .forms import TaskForm


def home(request):
    return render(request, 'index.html')


def projectList(request):
   projects = Project.objects.all()
   
   context = {'projects':projects}
   return render(request, 'projects/projects.html',context)


def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'projects/project-detail.html',context)


def taskList(request):
    user_tasks =Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)
 
    context = {'tasks':tasks,'user_tasks':user_tasks}
    return render(request, 'projects/tasks.html',context)


def taskDetail(request,pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'projects/task-detail.html',context)


def taskCreate(request):
   form = TaskForm
   if request.method == "POST":
       form =TaskForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('tasks')
        
   context = {'form':form}
   return render(request, 'projects/task-create.html',context)


def joinTask(request,pk):
   task =Task.objects.get(id=pk)
   task.assignee=request.user
   task.save()
   return redirect('tasks')


class ProjectCreateView(CreateView):
    model = Project
    fields = ["name","description"]
    template_name = 'projects/project_create_form.html'
    success_url = reverse_lazy('projects')

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'projects/project_update_form.html'
    fields = ["name","description"]
    success_url = reverse_lazy('projects')


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'projects/task_update_form.html'
    fields = ["title","description","project","assignee","due_date","status"]
    success_url = reverse_lazy('tasks')
    

class ProjectDeleteView(DeleteView):
   model = Project
   template_name = 'projects/project_confirm_delete.html'
   success_url = reverse_lazy('projects')

class TaskDeleteView(DeleteView):
   model = Task
   template_name = 'projects/task_confirm_delete.html'
   success_url = reverse_lazy('tasks')