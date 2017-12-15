from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from ..models import Officer
from .serializers import OfficerSerializer

from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers


class OfficerListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


class OfficerRetrieveAPIView(RetrieveAPIView):
    """
    This class API view is responsible for returning
    a single object/row in the table
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


class OfficerCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating a new account
    """
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer


class OfficerLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.OfficerLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = serializers.OfficerLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            data = serializer.data
            return Response(data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
