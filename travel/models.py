from django.db import models

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