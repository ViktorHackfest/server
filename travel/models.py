from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class City(models.Model):
    PROVINCE_CHOICES = [
        ('ACEH', 'Aceh'),
        ('SUMUT', 'Sumatera Utara'),
        ('SUMBAR', 'Sumatera Barat'),
        ('RIAU', 'Riau'),
        ('JAMBI', 'Jambi'),
        ('SUMSEL', 'Sumatera Selatan'),
        ('BENGKULU', 'Bengkulu'),
        ('LAMPUNG', 'Lampung'),
        ('BABEL', 'Kepulauan Bangka Belitung'),
        ('KEP. RIAU', 'Kepulauan Riau'),
        ('DKI JAKARTA', 'DKI Jakarta'),
        ('JAWA BARAT', 'Jawa Barat'),
        ('JAWA TENGAH', 'Jawa Tengah'),
        ('DI YOGYAKARTA', 'DI Yogyakarta'),
        ('JAWA TIMUR', 'Jawa Timur'),
        ('BANTEN', 'Banten'),
        ('BALI', 'Bali'),
        ('NTB', 'Nusa Tenggara Barat'),
        ('NTT', 'Nusa Tenggara Timur'),
        ('KALBAR', 'Kalimantan Barat'),
        ('KALTENG', 'Kalimantan Tengah'),
        ('KALSEL', 'Kalimantan Selatan'),
        ('KALTIM', 'Kalimantan Timur'),
        ('KALTARA', 'Kalimantan Utara'),
        ('SULUT', 'Sulawesi Utara'),
        ('SULTENG', 'Sulawesi Tengah'),
        ('SULSEL', 'Sulawesi Selatan'),
        ('SULTRA', 'Sulawesi Tenggara'),
        ('GORONTALO', 'Gorontalo'),
        ('SULBAR', 'Sulawesi Barat'),
        ('MALUKU', 'Maluku'),
        ('MALUT', 'Maluku Utara'),
        ('PAPUA', 'Papua'),
        ('PAPUA BARAT', 'Papua Barat'),
    ]

    name = models.CharField(max_length=100)
    province = models.CharField(max_length=50, choices=PROVINCE_CHOICES)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    traveler = models.ForeignKey("user.TravelerModel", on_delete=models.CASCADE)
    tour_guide = models.ForeignKey("user.TourGuideModel", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.BigIntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Booking: (id= {self.id}) | (traveler = {self.traveler.id}) | (destination = {self.destination.name}) | (date = {self.date}) | (price = {self.price}) | (status = {self.status})"
    
    def validate_date(self):
        if self.start_date > self.end_date:
            raise ValidationError("Start date must be before than end date")

    def validate_price(self):
        if self.price != 100000 * (self.end_date - self.start_date).days:
            raise ValidationError("Price is not valid")