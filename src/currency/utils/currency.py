from currency.utils.constants import MODE_CREDIT


def manage_transactions_into_wallet(wallet_obj, transaction_obj):
    if transaction_obj.mode in MODE_CREDIT:
        wallet_obj.total_earned += transaction_obj.amount
        wallet_obj.available_amount += transaction_obj.amount
    else:
        wallet_obj.total_spent += transaction_obj.amount
        wallet_obj.available_amount -= transaction_obj.amount

    wallet_obj.save()
