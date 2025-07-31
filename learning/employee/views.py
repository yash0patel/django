from django.shortcuts import render,redirect,get_object_or_404
from . import forms,models
# Create your views here.
def createEmployeeFormView(request):
    if request.method == "POST":
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
        else:
            form = forms.EmployeeForm()
    else:
        form = forms.EmployeeForm()

    return render(request,"employee/createemployee1.html",{'form':form})

def listEmployee(request):
    emp = models.employee1.objects.all().values()
    return render(request,"employee/listEmployee.html",{'employees':emp})

def delete_employee(request,pk):
    emp = models.employee1.objects.get(id=pk)
    if request.method == "POST":
        emp.delete()
        return redirect('list_employee')
    return render(request,"employee/delete_config.html",{'employee':emp})

def update_employee(request,pk):
    employee = get_object_or_404(models.employee1,pk=pk)

    if request.method == 'POST':
        form = forms.EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list_employee')
    else:
        form = forms.EmployeeForm(instance=employee)

    return render(request,'employee/update_employee.html',{'form':form})

def createPlayerFormView(request):
    if request.method == "POST":
        form = forms.PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_player')
    else:
        form = forms.PlayerForm()
    
    return render(request,'player/createplayer.html',{'form':form})

def listPlayer(request):
    player = models.player.objects.all().values()
    return render(request,"player/listplayer.html",{"player":player})

def delete_player(request,pk):
    player = models.player.objects.get(id = pk)
    if request.method == "POST":
        player.delete()
        return redirect('list_player')
    return render(request,"player/delete_config.html",{"player" : player})

def update_player(request,pk):
    player = get_object_or_404(models.player,pk=pk)

    if request.method == "POST":
        form = forms.PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('list_player')
        else:
            form = forms.PlayerForm(instance=player)
    else:
        form = forms.PlayerForm(instance=player)
    
    return render(request,"player/update_player.html",{'form':form})