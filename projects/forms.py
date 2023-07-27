from django.forms import ModelForm
from django.forms import DateInput

from .models import Project,Task


class TaskForm(ModelForm):
  class Meta:
      model =Task
      fields ='__all__'
      widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
               attrs={'type': 'date' }),
               }
      