from django.urls import path
from .views import RegisterAPIView, TourGuideListAPIView, TourGuideDetailAPIView, TravelerListAPIView

app_name = "user"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register_api"),
    path("tour-guide/", TourGuideListAPIView.as_view(), name="tour_guide_list_api"),
    path("traveler/", TravelerListAPIView.as_view(), name="traveler_list_api"),
    path(
        "tour-guide/<int:pk>/",
        TourGuideDetailAPIView.as_view(),
        name="tour_guide_detail_api",
    ),
]
