# third party imports
from simple_history.models import HistoricalRecords

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
    """
    Model to store per manufacturer's wallet information
    """
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.PROTECT)
    available_amount = models.FloatField(default=0)
    total_spent = models.FloatField(default=0)
    total_earned = models.FloatField(default=0)

    history = HistoricalRecords()

    def __str__(self):
        return self.manufacturer.name


class Transactions(RowInformation):
    """
    Model to store transaction details
    """
    wallet = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    amount = models.FloatField()
    mode = models.CharField(max_length=2, choices=VALID_MODES)

    history = HistoricalRecords(inherit=True, excluded_fields=['is_active'])

    def __str__(self):
        return "%s -- %s -- %s" % (self.wallet, self.amount, self.mode)

    @transaction.atomic()
    def save(self, *args, **kwargs):
        is_new_transaction = self.pk is None

        super(Transactions, self).save(*args, **kwargs)

        if is_new_transaction:
            manage_transactions_into_wallet(self.wallet, self)


class Sales(Transactions, RowInformation):
    """
    Model to store all sales details
    """
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
    """
    Model to store expenditure details
    """
    notes = models.TextField()

    def __str__(self):
        return "%s -- %s -- %s" % (self.wallet, self.amount, self.notes)

    def save(self, *args, **kwargs):
        if self.mode in MODE_CREDIT:
            raise ValidationError("Can't have credits in expenditures")

        super(Expenditures, self).save(*args, **kwargs)

