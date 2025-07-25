"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path('home/',views.home),
 path('about/',views.aboutus),
 path('contactus/',views.contactus),
 path('students/',views.studentList),
 path('productlist/',views.getProducts),
 path('swiggyuser/',views.getSwiggyUser),
 path('team/',views.getTeams),
 path('student/',views.getStudentDetail)
]
