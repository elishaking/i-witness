from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Officer
from .serializers import OfficerSerializer

class OfficerListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


class AccountRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

class AccountCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating a new account
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer