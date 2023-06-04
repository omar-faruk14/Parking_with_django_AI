from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    number_of_parking = models.IntegerField()
    parking_limit = models.IntegerField()
    parking_number_ratio = models.IntegerField()

    def __str__(self):
        return self.name