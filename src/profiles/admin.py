from django.contrib import admin

from profiles.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at', 'email', 'phone', 'designation')


admin.site.register(Person, PersonAdmin)
