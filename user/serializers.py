from rest_framework import serializers

from .models import TravelerModel, SellerModel, TourGuideModel
from travel.serializers import CitySerializer


class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelerModel
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = "__all__"


class TourGuideSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = TourGuideModel
        fields = "__all__"
