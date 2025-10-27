from django.contrib import admin
from .models import (
    Owner, Car, Technician, WorkType,
    ServicePrice, Service, ServiceRecord,
    SparePart, ServicePart
)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "email", "telefon")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("znacka", "model", "spz", "majitel")


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ("jmeno", "prijmeni", "specializace", "telefon")


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ("nazev",)


@admin.register(ServicePrice)
class ServicePriceAdmin(admin.ModelAdmin):
    list_display = ("worktype", "cena", "datum_od", "datum_do")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("car", "technician", "datum_servisu", "total_price")


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ("car", "datum_servisu", "typ_servisu", "technician")


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ("nazev", "cena", "skladova_zasoba")


@admin.register(ServicePart)
class ServicePartAdmin(admin.ModelAdmin):
    list_display = ("service_record", "spare_part", "mnozstvi", "aktualni_cena")
