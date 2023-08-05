from django.urls import path

from . import views

urlpatterns = [
    path('v1/projects/', views.ProjectList.as_view(), name='projects-api'),
    path('v1/projects/<int:pk>/', views.ProjectDetail.as_view(), name='projects-detail-api'),
    path('v1/tasks/', views.TaskList.as_view(), name='task-api'),
    path('v1/tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail-api'),
]


# path('register/', views.registration, name='register'),
# path('login/', views.UserLoginView.as_view(), name = 'login'),
# path('logout/', views.logout_user, name = 'logout'),
# path('update-profile/', views.update_profile, name ='update-profile'), 