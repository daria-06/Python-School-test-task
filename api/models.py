from django.db import models


# Create your models here.
class Driver(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='vehicles', blank=True, null=True)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    plate_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.make}({self.plate_number}): {self.driver_id}"