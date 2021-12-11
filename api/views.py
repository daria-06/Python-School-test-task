from rest_framework import serializers, viewsets
from rest_framework.views import APIView
from django.http import Http404
from .serializers import DriverSerializer, VehicleListSerializer, VehicleDetailSerializer, VehicleSetDriverSerializer
from .models import Driver, Vehicle
from rest_framework import status
from rest_framework.response import Response
from django_filters import FilterSet, BooleanFilter, DateFilter
from rest_framework import generics, mixins


class DriverFilter(FilterSet):
    """
    Driver filter to filter drivers by dates when they were created at
    """
    created_at__gte = DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = DateFilter(field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = Driver
        fields = {
            'created_at'
        }


class VehicleFilter(FilterSet):
    """
    Vehicle filter to see which vehicles are occupied
    """
    with_drivers = BooleanFilter(field_name='driver_id', lookup_expr='isnull', exclude=True)

    class Meta:
        model = Vehicle
        fields = {
            'driver_id'
        }


class DriverList(generics.ListCreateAPIView):
    """
    Class to view all drivers or create a new driver
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filterset_class = DriverFilter


class DriverDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class to view individual driver in detail, update or delete record
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class VehicleList(generics.ListCreateAPIView):
    """
    Class to view all vehicles or create a new vehicle
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleListSerializer
    filterset_class = VehicleFilter


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Class to view individual vehicle in detail, update it or delete it
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleDetailSerializer


class VehicleSetDriver(generics.RetrieveUpdateAPIView):
    """
    View individual vehicle and assign or remove a driver from a vehicle
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSetDriverSerializer