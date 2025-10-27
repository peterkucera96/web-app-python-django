from django import forms
from .models import Owner, Car, Service, SparePart


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['jmeno', 'prijmeni', 'adresa', 'telefon', 'email']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['znacka', 'model', 'rok_vyroby', 'vin', 'spz', 'majitel']


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['car', 'technician', 'datum_servisu', 'base_price', 'total_price', 'popis']


class SparePartForm(forms.ModelForm):
    class Meta:
        model = SparePart
        fields = ['nazev', 'popis', 'cena', 'skladova_zasoba']
