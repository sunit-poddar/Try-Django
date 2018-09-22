# third party imports

# django imports
from django.db import models

# project level imports
from try_django_utils.model_utils import RowInformation
from manufacturers.models import Manufacturer

# app level imports
from vehicles.utils.constants import VEHICLE_CHOICES


class VehicleInformation(RowInformation):
    name = models.CharField(max_length=400)
    type = models.CharField(max_length=3, choices=VEHICLE_CHOICES)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.PROTECT)
    number_of_doors = models.PositiveIntegerField()
    number_of_wheels = models.PositiveIntegerField()
    number_of_airbags = models.PositiveIntegerField()
    seating_capacity = models.PositiveIntegerField()
    steering_type = models.CharField(max_length=200)
    engine_type = models.CharField(max_length=200)
    engine_power = models.CharField(max_length=200)
    extras = models.TextField()
    number_of_drivers = models.PositiveIntegerField()
    number_of_engines = models.PositiveIntegerField()

    def __str__(self):
        return "%s - %s - %s" % (self.name, self.type, self.manufacturer)
