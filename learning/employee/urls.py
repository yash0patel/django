from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path("createEmployee1/",views.createEmployeeFormView),
 path("listEmployee/",views.listEmployee,name="list_employee"),
 path("deleteEmployee/<int:pk>/",views.delete_employee,name="delete_employee"),
 path("updateEmployee/<int:pk>",views.update_employee,name="update_employee"),
 
 path("createPlayer/",views.createPlayerFormView),
 path("listPlayer/",views.listPlayer,name="list_player"),
 path("deletePlayer/<int:pk>/",views.delete_player,name="delete_player"),
 path("updatePlayer/<int:pk>",views.update_player,name="update_player"),
]
