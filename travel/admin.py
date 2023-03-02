from django.contrib import admin
from .models import City, Destination, Booking


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

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    fields = [
        'traveler',
        'tour_guide',
        'start_date',
        'end_date',
        'price',
        'status'
    ]
    list_display = [
        'traveler',
        'tour_guide',
        'start_date',
        'end_date',
        'price',
        'status'
    ]