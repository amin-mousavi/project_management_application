from django.contrib import admin

from.models import Project,Task


class TaskInline(admin.StackedInline):
    model = Task
    extra = 2

class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline, ]
    list_display = ['name', 'date_created']
    search_fields = ['name', 'description']
    list_filter = ['date_created',]

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assignee', 'project', 'date_created', 'due_date', 'status']
    search_fields = ['title', 'assignee', 'project', 'status', 'description']
    list_filter = ['assignee', 'project', 'status', 'date_created', 'due_date']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)