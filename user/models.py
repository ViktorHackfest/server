from django.db import models



class TravelerModel(models.Model):
    id = models.AutoField(primary_key=True)
    displayName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.BigIntegerField()

    def __str__(self):
        return f"Traveler: {self.displayName} - (id= {self.id})"


class TourGuideModel(models.Model):
    id = models.AutoField(primary_key=True)
    displayName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return f"Tour Guide: {self.displayName} - (id= {self.id})"


class SellerModel(models.Model):
    id = models.AutoField(primary_key=True)
    displayName = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phoneNumber = models.BigIntegerField()
    address = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"Seller: {self.displayName} - (id= {self.id})"
