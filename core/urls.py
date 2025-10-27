from django.urls import path
from . import views

urlpatterns = [
    path('owners/', views.owners_list, name='owners_list'),
    path('owners/<int:owner_id>/', views.owner_detail, name='owner_detail'),
    path('owners/add/', views.add_owner, name='add_owner'),

    path('cars/', views.cars_list, name='cars_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/add/', views.add_car, name='add_car'),

    path('services/', views.services_list, name='services_list'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('services/add/', views.add_service, name='add_service'),

    path('technicians/', views.technician_list, name='technician_list'),
    path('spareparts/add/', views.add_sparepart, name='add_sparepart'),
    path('records/', views.service_record_list, name='service_record_list'),

    path('', views.homepage, name='homepage'),
    path('cars/delete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('owners/delete/<int:owner_id>/', views.delete_owner, name='delete_owner'),



]
