from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Device

# Create your views here.


@login_required
def device_list(request):
    devices = Device.objects.all()
    return render(request, 'core/device_list.html', {'devices': devices})


@login_required
def add_device(request):
    if request.method == 'POST':
        # Handle form submission and create new device
        pass  # Add your code here
    else:
        return render(request, 'core/add_device.html')
