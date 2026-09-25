from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import ReportService


class PublicReportAPIView(APIView):

    permission_classes = [AllowAny]


class KPIApiView(PublicReportAPIView):


    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.kpi(days))


class RevenueByDayApiView(PublicReportAPIView):


    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.revenue_by_day(days))


class TopModelsApiView(PublicReportAPIView):


    def get(self, request):
        limit = int(request.GET.get("limit", 5))
        return Response(ReportService.top_models(limit))


class ManagerLoadApiView(PublicReportAPIView):


    def get(self, request):
        days = int(request.GET.get("days", 30))
        return Response(ReportService.manager_load(days))


class StockApiView(PublicReportAPIView):


    def get(self, request):
        return Response(ReportService.stock_status())
