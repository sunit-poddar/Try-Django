
def create_manufacturer_wallet(manufacturer_obj):
    """
    Create Wallet entry after new manufacturer is created
    :param manufacturer_obj: manufacturer object
    :return: None
    """
    from currency.models import Wallet

    wallet_obj = Wallet(manufacturer=manufacturer_obj)
    wallet_obj.save()

    return
