# Python School Test Task

This is a test task for Yalantis Python School 2022: REST API using Python, Django, DRF and django-filters. All information is sent and displayed in JSON format.

## Task (brief version)

Розробіть REST API для парку машин з водіями

Створіть таблиці (моделі) - Driver + Vehicle

Створіть перелік відкритих (без аутентифікацій) endpointів

## Usage

After setting it up as described in SETUP.md and running the project using ```python manage.py runserver```, you can use either POSTMAN or go directly to http://127.0.0.1:8000/ in browser for testing it

### Endpoints and methods

POST `/drivers/driver/` - add new driver

GET `/drivers/driver/` - show all drivers

GET `/drivers/driver/<driver_id>/` - show driver by ID

UPDATE `/drivers/driver/<driver_id>/` - edit driver info

DELETE `/drivers/driver/<driver_id>/` - delete driver


POST `/vehicles/vehicle/` - add new vehicle

GET `/vehicles/vehicle/` - show all vehicles

GET `/vehicles/vehicle/<vehicle_id>` - show vehicle info by ID

UPDATE `/vehicles/vehicle/<vehicle_id>/` - edit vehicle info

DELETE `/vehicles/vehicle/<vehicle_id>/` - delete vehicle

(POST) UPDATE* `/vehicles/set_driver/<vehicle_id>/` - putting driver in the vehicle/removing driver from the vehicle (you are required to put driver ID in JSON or set it to null to remove driver from the car)

\* I could not figure out how to implement POST as required here, that is why I implemented UPDATE

### Filters

GET `/drivers/driver/?created_at__gte=2021-12-08` - show drivers created after 08-12-2021

GET `/drivers/driver/?created_at__lte=2021-12-09` - show drivers created after 09-12-2021

GET `/vehicles/vehicle/?with_drivers=true` - show vehicles with drivers

GET `/vehicles/vehicle/?with_drivers=false` - show vehicles without drivers
