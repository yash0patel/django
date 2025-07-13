from django.shortcuts import render
from . import forms,models
# Create your views here.

def createEmployeeForm(request):
    employeeform = forms.EmployeeForm()
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            emp = models.Employee(**form.cleaned_data)
            emp.save()
    return render(request,"employee/EmployeeForm.html",{"form":employeeform})


