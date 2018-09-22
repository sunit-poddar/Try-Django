# third party imports
from simple_history.models import HistoricalRecords

# django imports
from django.db import models

# project level imports
from try_django_utils.model_utils import RowInformation


class Person(RowInformation):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=200)

    history = HistoricalRecords()

    def __str__(self):
        return self.name
