from django.contrib import admin
from . import models


@admin.register(models.TravelerModel)
class UserAdmin(admin.ModelAdmin):
    fields = [
        'displayName',
        'email',
        'phoneNumber',
    ]
    list_display = [
        'id',
        'displayName',
        'email',
        'phoneNumber',
    ]


@admin.register(models.TourGuideModel)
class TourGuideAdmin(admin.ModelAdmin):
    fields = [
        'displayName',
        'email',
        'phoneNumber',
        'address',
    ]

    list_display = [
        'id',
        'displayName',
        'email',
        'phoneNumber',
        'address',
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
