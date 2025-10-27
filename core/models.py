from django.db import models


class Owner(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    adresa = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"


class Car(models.Model):
    znacka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rok_vyroby = models.IntegerField()
    vin = models.CharField(max_length=50)
    spz = models.CharField(max_length=20)
    majitel = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.znacka} {self.model} ({self.spz})"


class Technician(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    specializace = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"


class WorkType(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()

    def __str__(self):
        return self.nazev


class ServicePrice(models.Model):
    worktype = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    datum_od = models.DateField()
    datum_do = models.DateField()

    def __str__(self):
        return f"{self.worktype.nazev} - {self.cena} Kč"


class Service(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    datum_servisu = models.DateField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    popis = models.TextField()

    def __str__(self):
        return f"Servis {self.id} - {self.car.spz}"


class ServiceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    datum_servisu = models.DateField()
    typ_servisu = models.CharField(max_length=100)
    popis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    technician = models.ForeignKey(Technician, on_delete=models.CASCADE)
    worktype = models.ForeignKey(WorkType, on_delete=models.CASCADE)

    def __str__(self):
        return f"Záznam {self.id} - {self.car.spz}"


class SparePart(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    skladova_zasoba = models.IntegerField()

    def __str__(self):
        return self.nazev


class ServicePart(models.Model):
    service_record = models.ForeignKey(ServiceRecord, on_delete=models.CASCADE)
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)
    mnozstvi = models.IntegerField()
    aktualni_cena = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.mnozstvi}x {self.spare_part.nazev}"
