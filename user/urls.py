from django.urls import path
from .views import RegisterAPIView, TourGuideListAPIView, TourGuideDetailAPIView

app_name = "user"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register_api"),
    path("tour_guide/", TourGuideListAPIView.as_view(), name="tour_guide_list_api"),
    path("tour_guide/<int:pk>/", TourGuideDetailAPIView.as_view(), name="tour_guide_detail_api"),
]