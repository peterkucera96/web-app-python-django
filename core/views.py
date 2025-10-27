from django.shortcuts import render, get_object_or_404, redirect
from .models import Owner, Car, Service, Technician, SparePart, ServiceRecord
from .forms import OwnerForm, CarForm, ServiceForm, SparePartForm


def owners_list(request):
    owners = Owner.objects.all()
    return render(request, 'owners/list.html', {'owners': owners})


def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, id=owner_id)
    return render(request, 'owners/detail.html', {'owner': owner})


def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'cars/detail.html', {'car': car})


def services_list(request):
    services = Service.objects.all()
    return render(request, 'services/list.html', {'services': services})


def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/detail.html', {'service': service})

def homepage(request):
    return render(request, 'homepage.html')

def add_owner(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owners_list')
    else:
        form = OwnerForm()
    return render(request, 'owners/form.html', {'form': form})


def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = CarForm()
    return render(request, 'cars/form.html', {'form': form})

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    car.delete()
    return redirect('cars_list')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Owner

def delete_owner(request, owner_id):
    owner = get_object_or_404(Owner, id=owner_id)
    owner.delete()
    return redirect('owners_list')


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services_list')
    else:
        form = ServiceForm()
    return render(request, 'services/form.html', {'form': form})


def add_sparepart(request):
    if request.method == 'POST':
        form = SparePartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spareparts_list')
    else:
        form = SparePartForm()
    return render(request, 'spareparts/form.html', {'form': form})


def technician_list(request):
    technicians = Technician.objects.all()
    return render(request, 'technicians/list.html', {'technicians': technicians})


def service_record_list(request):
    records = ServiceRecord.objects.all()
    return render(request, 'records/list.html', {'records': records})
