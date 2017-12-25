from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Report
from .serializers import ReportSerializer, MediaSerializer


# Report api
class ReportListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating a new account
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
