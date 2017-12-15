from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Report, Media
from .serializers import ReportSerializer, MediaSerializer

#Report api
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


#Media api
class MediaListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

class MediaCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating a new account
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer