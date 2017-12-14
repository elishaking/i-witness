from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Witness
from .serializers import WitnessSerializer

class WitnessListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer


class WitnessRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer

class WitnessCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating a new account
    """
    queryset = Witness.objects.all()
    serializer_class = WitnessSerializer