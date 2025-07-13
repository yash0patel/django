from django import forms
from . import models

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100,label="Name")
    email = forms.EmailField(label="Email")
    department = forms.ChoiceField(
        choices=models.Employee.DEPARTMENT_CHOICES,
        label="Department",
        widget=forms.Select
    )
    salary = forms.DecimalField(label="Salary",max_digits=10,decimal_places=2)
    joining_date = forms.DateField(
        label="Joining Date",
        widget=forms.DateInput(attrs={'type':'date'})
    )