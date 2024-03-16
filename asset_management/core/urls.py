from django.urls import path
from . import views


urlpatterns = [
    path('', views.device_list, name='device-list'),
    path('device/<int:pk>/', views.device_detail, name='device-detail'),
    path('employee/', views.employee_list, name='employee-list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee-detail'),
    path('login/', views.login_view, name='login'),
]
