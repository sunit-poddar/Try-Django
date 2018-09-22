from django.contrib import admin

from vehicles.models import VehicleInformation


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at', 'type', 'manufacturer')


admin.site.register(VehicleInformation, VehicleAdmin)