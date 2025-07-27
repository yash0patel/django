from django import forms
from . import models

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = models.employee1
        fields = '__all__'
        widgets = {
            'date' : forms.DateInput(attrs={'type':'date'})
        }
        