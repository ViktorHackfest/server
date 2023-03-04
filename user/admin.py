from django.contrib import admin
from . import models


@admin.register(models.TravelerModel)
class UserAdmin(admin.ModelAdmin):
    fields = [
        "id",
        "money",
    ]
    list_display = [
        "id",
        "money",
    ]


@admin.register(models.TourGuideModel)
class TourGuideAdmin(admin.ModelAdmin):
    fields = [
        "id",
        "city",
        "name",
        "photo_url",
    ]

    list_display = [
        "id",
        "city",
        "name",
        "photo_url",
    ]


@admin.register(models.SellerModel)
class SellerAdmin(admin.ModelAdmin):
    fields = ["displayName", "email", "phoneNumber", "address", "rating"]

    list_display = ["id", "displayName", "email", "phoneNumber", "address", "rating"]
