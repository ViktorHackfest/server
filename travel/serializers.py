from rest_framework import serializers

from .models import City, Destination, Booking


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"


class DestinationListSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Destination
        fields = ("id", "name", "city")


class DestinationDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Destination
        fields = ("id", "name", "city", "description")


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            "traveler",
            "tour_guide",
            "start_date",
            "end_date",
            "price",
            "is_offline",
            "status",
        ]
