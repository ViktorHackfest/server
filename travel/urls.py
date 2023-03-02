from django.urls import path
from .views import (
    CityListAPIView,
    CityDetailAPIView,
    DestinationListAPIView,
    DestinationDetailAPIView,
    BookingListAPIView,
    BookingDetailAPIView,
)

app_name = "travel"

urlpatterns = [
    path("cities/", CityListAPIView.as_view(), name="city_list_api"),
    path("cities/<int:pk>/", CityDetailAPIView.as_view(), name="city_detail_api"),
    path(
        "destinations/", DestinationListAPIView.as_view(), name="destination_list_api"
    ),
    path(
        "destinations/<int:pk>/",
        DestinationDetailAPIView.as_view(),
        name="destination_detail_api",
    ),
    path("bookings/", BookingListAPIView.as_view(), name="booking_list_api"),
    path(
        "bookings/<int:pk>/", BookingDetailAPIView.as_view(), name="booking_detail_api"
    ),
]
