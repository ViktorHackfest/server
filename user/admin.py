from django.contrib import admin
from . import models


@admin.register(models.TravelerModel)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'uang',
    ]
    list_display = [
        'id',
        'uang',
    ]


@admin.register(models.TourGuideModel)
class TourGuideAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'city',
    ]

    list_display = [
        'id',
        'city',
    ]


@admin.register(models.SellerModel)
class SellerAdmin(admin.ModelAdmin):
    fields = [
        'displayName',
        'email',
        'phoneNumber',
        'address',
        'rating'
    ]

    list_display = [
        'id',
        'displayName',
        'email',
        'phoneNumber',
        'address',
        'rating'
    ]
