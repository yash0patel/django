from django.shortcuts import render
from . import forms,models
from django.contrib.auth.hashers import make_password 

def createEmployeeForm(request):
    employeeform = forms.EmployeeForm()
    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            emp = models.Employee(**form.cleaned_data)
            emp.save()
    return render(request,"employee/EmployeeForm.html",{"form":employeeform})

def createSignupForm(request):
    employeeSignupForm = forms.EmployeeSignupForm()
    if request.method == 'POST':
        form = forms.EmployeeSignupForm(request.POST)
        if form.is_valid():
            cleaned = form.cleaned_data
            singupForm = models.EmployeeSignup(
                name = cleaned['name'],
                email = cleaned['email'],
                password = make_password(cleaned['password'])
            )
            singupForm.save()
    return render(request,"employee/SignupForm.html",{"signupForm":employeeSignupForm})
