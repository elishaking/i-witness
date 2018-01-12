from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Witness
from .serializers import WitnessSerializer, WitnessCreateSerializer

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers


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
    This class API view is responsible for creating a new witness
    """
    queryset = Witness.objects.all()
    serializer_class = WitnessCreateSerializer


class WitnessLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.WitnessLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.WitnessLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response(data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
