from django import forms
from .models import *

class Form_posttask(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['description', 'deadline']