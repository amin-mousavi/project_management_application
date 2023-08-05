from django.urls import path

from . import views

urlpatterns = [
    path('v1/projects/', views.ProjectList.as_view(), name='projects-api'),
    path('v1/projects/<int:pk>/', views.ProjectDetail.as_view(), name='projects-detail-api'),
    path('v1/tasks/', views.TaskList.as_view(), name='task-api'),
    path('v1/tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail-api'),
]
