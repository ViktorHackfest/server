from django.contrib import admin
from .models import City, Destination


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'province'
    ]
    list_display = [
        'name',
        'province'
    ]


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'city',
        'description'
    ]
    list_display = [
        'name',
        'city',
        'description'
    ]
