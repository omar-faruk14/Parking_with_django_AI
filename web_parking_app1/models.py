from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    number_of_parking = models.IntegerField()
    parking_limit = models.IntegerField()

    def __str__(self):
        return self.name

class VehicleEntry(models.Model):
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    vehicle_registration_Name = models.CharField(max_length=255, unique=True, null=False)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.vehicle_name