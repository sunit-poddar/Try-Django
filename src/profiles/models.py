from django.db import models

from try_django_utils.model_utils import RowInformation

# Create your models here.


class Person(RowInformation):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    designation = models.CharField(max_length=200)

    def __str__(self):
        return self.name
