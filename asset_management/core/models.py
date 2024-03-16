from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

class Device(models.Model):
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    checked_out = models.BooleanField(default=False)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='checked_out_devices')
    checked_out_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checked_out_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    checked_out_date = models.DateTimeField(auto_now_add=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.CharField(max_length=100)
    condition_on_return = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.device.name} - {self.checked_out_date}"
    
    