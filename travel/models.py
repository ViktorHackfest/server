from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    province = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name