from rest_framework import filters, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):


    queryset = Order.objects.select_related("client", "car__brand", "manager").all()
    serializer_class = OrderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["client__full_name", "car__model", "car__brand__name"]
    ordering_fields = ["created_at", "total_amount", "status"]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        order = self.get_object()
        order.complete()
        return Response(self.get_serializer(order).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        order = self.get_object()
        order.cancel()
        return Response(self.get_serializer(order).data, status=status.HTTP_200_OK)
