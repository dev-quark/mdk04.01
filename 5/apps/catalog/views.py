








from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Brand, Car
from .serializers import BrandSerializer, CarSerializer


class BrandViewSet(viewsets.ModelViewSet):


    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "country"]


class CarViewSet(viewsets.ModelViewSet):


    queryset = Car.objects.select_related("brand").all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["brand", "status", "fuel_type", "year"]
    search_fields = ["model", "vin", "brand__name"]
    ordering_fields = ["price", "year", "created_at"]
