from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("employeeForm/",views.createEmployeeForm),
    path("signupForm/",views.createSignupForm)
]
