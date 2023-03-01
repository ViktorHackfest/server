from django.db import models
from travel.models import City


class TravelerModel(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    uang = models.BigIntegerField()

    def __str__(self):
        return f"Traveler: (id= {self.id}) | (uang = {self.uang})"


class TourGuideModel(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tour Guide: (id= {self.id}) | (city = {self.city.name}) | (province = {self.city.province})"


class SellerModel(models.Model):
    id = models.CharField(max_length=500, primary_key=True)
    displayName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.BigIntegerField()
    address = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Seller: {self.displayName} - (id= {self.id})"
