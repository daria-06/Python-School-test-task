from rest_framework import serializers
from .models import Driver, Vehicle

class DriverSerializer(serializers.ModelSerializer):
    """
    Serializer for driver model, provides information about drivers
    """
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Driver
        fields = ['id', 'first_name', 'last_name', 'created_at', 'updated_at']


class VehicleListSerializer(serializers.ModelSerializer):
    """
    Serializer for vehicle model, provides list of vehicles including driver name
    """
    # display driver's name below driver_id in a user friendly way
    driver_name = serializers.CharField(source='driver_id', read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_name', 'make', 'model', 'plate_number', 'created_at', 'updated_at']


class VehicleDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for vehicle model, provides basic details of vehicle
    """
    driver_name = serializers.CharField(source='driver_id', read_only=True)
    created_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%d/%m/%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Vehicle
        fields = ['driver_name', 'driver_id', 'make', 'model', 'plate_number', 'created_at', 'updated_at']


class VehicleSetDriverSerializer(serializers.ModelSerializer):
    """
    Serializer for vehicle model, used to assign or remove a driver from a vehicle
    """
    id = serializers.CharField(read_only=True)
    driver_name = serializers.CharField(source='driver_id', read_only=True)
    make = serializers.CharField(read_only=True)
    model = serializers.CharField(read_only=True)
    plate_number = serializers.CharField(read_only=True)

    class Meta:
        model = Vehicle
        fields = ['id', 'driver_id', 'driver_name', 'make', 'model', 'plate_number']

    def create(self, validated_data):
        vehicle = Vehicle.objects.update_or_create(
            pk=validated_data.get('pk', None),
            defaults={'driver_id': validated_data.get("driver_id")}
        )
        return vehicle