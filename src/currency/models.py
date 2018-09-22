# django imports
from django.db import models, transaction
from django.core.exceptions import ValidationError

# project level imports
from try_django_utils.model_utils import RowInformation
from manufacturers.models import Manufacturer
from vehicles.models import VehicleInformation

# app level imports
from currency.utils.constants import VALID_MODES, MODE_DEBIT, MODE_CREDIT
from currency.utils.currency import manage_transactions_into_wallet

class Wallet(RowInformation):
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.PROTECT)
    available_amount = models.FloatField()
    total_spent = models.FloatField()
    total_earned = models.FloatField()

    def __str__(self):
        return self.manufacturer.name


class Transactions(RowInformation):
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    amount = models.FloatField()
    mode = models.CharField(max_length=2, choices=VALID_MODES)

    def __str__(self):
        return "%s -- %s -- %s" % (self.wallet, self.amount, self.mode)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        is_new_transaction = self.pk is None

        super(Transactions, self).save(*args, **kwargs)

        if is_new_transaction:
            manage_transactions_into_wallet(self.wallet, self)


class Sales(Transactions, RowInformation):
    vehicle = models.ForeignKey(VehicleInformation, on_delete=models.PROTECT)
    timestamp = models.DateTimeField()
    reference_number = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "%s -- %s -- %s" % (self.wallet, self.amount, self.quantity)

    def save(self, *args, **kwargs):
        if self.mode in MODE_DEBIT:
            raise ValidationError("Can't have debits in sales")

        super(Sales, self).save(*args, **kwargs)


class Expenditures(Transactions, RowInformation):
    notes = models.TextField()

    def __str__(self):
        return "%s -- %s -- %s" % (self.wallet, self.amount, self.notes)

    def save(self, *args, **kwargs):
        if self.mode in MODE_CREDIT:
            raise ValidationError("Can't have credits in expenditures")

        super(Expenditures, self).save(*args, **kwargs)

