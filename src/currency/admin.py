from django.contrib import admin

from currency.models import Wallet, Sales, Transactions, Expenditures


class WalletAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'created_at', 'modified_at', 'available_amount', 'total_spent', 'total_earned')


class SalesAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'vehicle', 'created_at', 'timestamp', 'reference_number', 'quantity', 'amount'
                    , 'mode')


class ExpendituresAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'created_at', 'amount', 'mode', 'notes')


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transactions)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Expenditures, ExpendituresAdmin)
