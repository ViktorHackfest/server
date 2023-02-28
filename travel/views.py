from django_filters import rest_framework as filters
from rest_framework import generics
from .models import City, Destination
from .serializers import CitySerializer, DestinationListSerializer, DestinationDetailSerializer

class DestinationFilter(filters.FilterSet):
    city = filters.CharFilter(field_name='city__name', lookup_expr='icontains')
    province = filters.ChoiceFilter(choices=City.PROVINCE_CHOICES, field_name='city__province')

    class Meta:
        model = Destination
        fields = ['city', 'province']


class CityListAPIView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DestinationListAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = DestinationFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return DestinationListSerializer
        return DestinationDetailSerializer


class DestinationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailSerializer