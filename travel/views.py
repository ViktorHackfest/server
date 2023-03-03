from django_filters import rest_framework as filters
from rest_framework import generics, status
from rest_framework.response import Response
from django.core.exceptions import ValidationError

from .models import City, Destination, Booking
from .serializers import (
    CitySerializer,
    DestinationListSerializer,
    DestinationDetailSerializer,
    BookingSerializer,
)


class DestinationFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")
    city = filters.CharFilter(field_name="city__name", lookup_expr="icontains")
    province = filters.ChoiceFilter(
        choices=City.PROVINCE_CHOICES, field_name="city__province"
    )

    class Meta:
        model = Destination
        fields = ["name", "city", "province"]


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class DestinationListAPIView(generics.ListAPIView):
    queryset = Destination.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DestinationFilter
    serializer_class = DestinationListSerializer


class DestinationDetailAPIView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer


class BookingListAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_queryset(self):
        traveler = self.request.META.get("HTTP_X_FIREBASE_ID")
        return self.queryset.filter(traveler=traveler)

    def create(self, request, *args, **kwargs):
        try:
            traveler = self.request.META.get("HTTP_X_FIREBASE_ID")
            data = request.data.copy()
            data["traveler"] = traveler
            print(data)
            serializer = self.get_serializer(data=data)
            print(serializer)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        booking = serializer.save()
        booking.validate_price()
        booking.validate_date()
        booking.validate_billing()
        booking.traveler.money = booking.traveler.money - booking.price
        booking.traveler.save()


class BookingDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_object(self):
        traveler = self.request.META.get("HTTP_X_FIREBASE_ID")
        return self.queryset.get(traveler=traveler, id=self.kwargs["pk"])

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop("partial", False)
            instance = self.get_object()
            allowed_fields = [
                "status",
            ]  # list of fields that can be updated
            # Check if the updated fields are allowed
            for field in request.data.keys():
                if field not in allowed_fields:
                    return Response(
                        {"error": f"Field '{field}' is not allowed."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            # Update the allowed fields
            serializer = self.get_serializer(
                instance, data=request.data, partial=partial
            )
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": e.message}, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        booking = serializer.save()
        booking.validate_price()
        booking.validate_date()
        booking.validate_billing()
        booking.traveler.money = (
            booking.traveler.money + booking.price * 70 / 100
        )
        booking.traveler.save()
