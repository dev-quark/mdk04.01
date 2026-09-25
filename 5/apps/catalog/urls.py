from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BrandViewSet, CarViewSet

app_name = "catalog"

router = DefaultRouter()
router.register(r"brands", BrandViewSet, basename="brands")
router.register(r"cars", CarViewSet, basename="cars")

urlpatterns = [
    path("", include(router.urls)),
]
