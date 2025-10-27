# AutoServis – Django Webová Aplikace

Jednoduchý servisný informačný systém pre evidenciu áut, zákazníkov, servisov, technikov a náhradných dielov. Projekt bol vytvorený v rámci predmetu DS II ako webová aplikácia pomocou Django frameworku.

---

## Funkcionalita

- Evidencia majiteľov a ich áut
- Záznamy o servise, vrátane technikov a náhradných dielov
- Pridávanie a editácia záznamov cez formuláre
- Admin rozhranie pre správu údajov
- REST API pomocou Django Ninja
- Bootstrap dizajn a jednoduché rozhranie

---

## Modely

Projekt obsahuje nasledovné prepojené modely:

- `Owner` – Majiteľ auta
- `Car` – Vozidlo
- `Technician` – Technik
- `Service` – Servisný zásah
- `ServiceRecord` – Podrobný záznam servisu
- `SparePart` – Náhradné diely
- `ServicePart` – Spojenie dielov so servisom
- `WorkType`, `ServicePrice` – Typy prác a ich ceny

---

## Spustenie projektu

### 1. Klonovanie a prostredie:

```bash
git clone https://github.com/peterkucera96/web-app-python-django.git
cd autoservis
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### 2. Migrácie a superužívateľ:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 3. Prihlásenie

- URL: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
- Username: admin
- Password: admin

---

### 4. Spustenie vývojového servera:

```bash
python manage.py runserver
```

Otvor v prehliadači: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## REST API

Realizované pomocou **Django Ninja**.

- Swagger dokumentácia: [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)
- Príklady:
  - `/api/cars/`
  - `/api/owners/`
  - `/api/services/`
  - `/api/technicians/`

---

## Technológie

- Python 3.11
- Django 5.x
- SQLite
- Bootstrap 5 (CDN)
- HTML/CSS
- Django Ninja (REST API)

---

## 👤 Autor

Peter Kučera  
VŠB – Vysoká škola báňska V Ostrave
Predmet: SKJ 
Rok: 2025