from django.core.exceptions import ValidationError

from currency.utils.constants import MODE_CREDIT


def manage_transactions_into_wallet(wallet_obj, transaction_obj):
    """
    Manage transactions into wallet depending on transaction modes
    :param wallet_obj: Wallet object
    :param transaction_obj: Transaction object
    :return: None
    """
    if transaction_obj.mode in MODE_CREDIT:
        wallet_obj.total_earned += transaction_obj.amount
        wallet_obj.available_amount += transaction_obj.amount
    else:
        wallet_obj.total_spent += transaction_obj.amount
        wallet_obj.available_amount -= transaction_obj.amount

    if wallet_obj.available_amount < 0:
        raise ValidationError('Not enough money')

    wallet_obj.save()

    return
