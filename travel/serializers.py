from rest_framework import serializers

from .models import City, Destination, Booking

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'province')

class DestinationListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Destination
        fields = ('id', 'name', 'city')

class DestinationDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)

    class Meta:
        model = Destination
        fields = ('id', 'name', 'city', 'description')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'