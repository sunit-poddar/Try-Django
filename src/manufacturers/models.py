# third party
from simple_history.models import HistoricalRecords

from django.db import models

# project level imports
from try_django_utils.model_utils import RowInformation
from profiles.models import Person

# app level imports
from manufacturers.utils.manufacturer import create_manufacturer_wallet


class Manufacturer(RowInformation):
    """
    Model to store Manufacturer details
    """
    name = models.CharField(max_length=200)
    number_of_employee = models.PositiveIntegerField()
    establishment = models.DateField()
    website = models.URLField()
    ceo = models.ForeignKey(Person, on_delete=models.PROTECT)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        is_new_manufacturer = self.pk is None
        super(Manufacturer, self).save(*args, **kwargs)

        if is_new_manufacturer:
            create_manufacturer_wallet(self)
