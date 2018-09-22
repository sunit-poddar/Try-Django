from django.db import models

# project level imports
from try_django_utils.model_utils import RowInformation
from profiles.models import Person


class Manufacturer(RowInformation):
    name = models.CharField(max_length=200)
    number_of_employee = models.PositiveIntegerField()
    establishment = models.DateField()
    website = models.URLField()
    ceo = models.ForeignKey(Person, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
