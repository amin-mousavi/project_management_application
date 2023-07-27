from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home, name = 'home'),
    path('projects/', views.projectList, name = 'projects'),
    path('projects/<int:pk>', views.projectDetail, name ='project-detail'), 
    path('tasks', views.taskList, name ='tasks'),
    path('tasks/<int:pk>', views.taskDetail, name ='task-detail'),
    path('create-task', views.taskCreate, name ='create-task'),
    path('create-project', views.ProjectCreateView.as_view(), name ='create-project'),
]
