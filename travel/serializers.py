from rest_framework import serializers

from .models import City, Destination

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