# devices/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Device, Employee

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'core/device_list.html', {'devices': devices})

@login_required
def device_detail(request, pk):
    device = Device.objects.get(pk=pk)
    return render(request, 'core/device_detail.html', {'device': device})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employee_list.html', {'employees': employees})

@login_required
def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    return render(request, 'core/employee_detail.html', {'employee': employee})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('device-list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'core/login.html')
