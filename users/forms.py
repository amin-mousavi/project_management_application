from django import forms
from django.forms import ModelForm

from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model =Profile
        fields = ['first_name', 'last_name', 'email','bio','photo']
        
    email = forms.EmailField(required=True)