from django.contrib import admin

from manufacturers.models import Manufacturer

# Register your models here.


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'establishment', 'number_of_employee', 'website', 'ceo')


admin.site.register(Manufacturer, ManufacturerAdmin)