from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('drivers/driver/', views.DriverList.as_view()),
    path('drivers/driver/<int:pk>/', views.DriverDetail.as_view()),
    path('vehicles/vehicle/', views.VehicleList.as_view()),
    path('vehicles/vehicle/<int:pk>/', views.VehicleDetail.as_view()),
    path('vehicles/set_driver/<int:pk>/', views.VehicleSetDriver.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

