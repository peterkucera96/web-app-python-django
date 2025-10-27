from .models import Car, Owner, Service, Technician
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI

api = NinjaAPI()


# ========== CARS ==========
@api.get("/cars/")
def list_cars(request):
    return [{"id": c.id, "znacka": c.znacka, "model": c.model, "spz": c.spz} for c in Car.objects.all()]


@api.get("/cars/{car_id}")
def get_car(request, car_id: int):
    car = get_object_or_404(Car, id=car_id)
    return {
        "id": car.id,
        "znacka": car.znacka,
        "model": car.model,
        "rok": car.rok_vyroby,
        "spz": car.spz,
        "majitel": str(car.majitel)
    }


# ========== OWNERS ==========
@api.get("/owners/")
def list_owners(request):
    return [{"id": o.id, "meno": f"{o.jmeno} {o.prijmeni}", "email": o.email} for o in Owner.objects.all()]


@api.get("/owners/{owner_id}")
def get_owner(request, owner_id: int):
    owner = get_object_or_404(Owner, id=owner_id)
    return {
        "id": owner.id,
        "meno": owner.jmeno,
        "priezvisko": owner.prijmeni,
        "email": owner.email,
        "telefon": owner.telefon
    }


# ========== SERVICES ==========
@api.get("/services/")
def list_services(request):
    return [{"id": s.id, "car": s.car.spz, "technician": str(s.technician), "datum": s.datum_servisu.strftime("%Y-%m-%d")} for s in Service.objects.all()]


# ========== TECHNICIANS ==========
@api.get("/technicians/")
def list_technicians(request):
    return [{"id": t.id, "meno": f"{t.jmeno} {t.prijmeni}", "specializace": t.specializace} for t in Technician.objects.all()]

