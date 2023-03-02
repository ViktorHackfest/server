from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import TourGuideModel
from .serializers import TravelerSerializer, TourGuideSerializer


class RegisterAPIView(APIView):
    def post(self, request, format=None):
        type_user = request.query_params.get("type_user", None)
        if type_user == "traveler":
            serializer_class = TravelerSerializer
        elif type_user == "tour_guide":
            serializer_class = TourGuideSerializer
        else:
            return Response({"success": False})

        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response({"success": True, "user_data": user_data})


class TourGuideListAPIView(generics.ListCreateAPIView):
    queryset = TourGuideModel.objects.all()
    serializer_class = TourGuideSerializer


class TourGuideDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourGuideModel.objects.all()
    serializer_class = TourGuideSerializer
