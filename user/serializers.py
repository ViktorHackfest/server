from rest_framework import serializers
from .models import TravelerModel, SellerModel, TourGuideModel


class TravelerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelerModel
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SellerModel
        fields = "__all__"


class TourGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourGuideModel
        fields = "__all__"
