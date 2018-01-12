from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from ..models import Media
from .serializers import MediaSerializer, MediaCreateSerializer


class MediaListAPIView(ListAPIView):
    """
    This class API view is responsible for returning
    the entire table content
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class MediaCreateAPIView(CreateAPIView):
    """
    This class API view is responsible for creating new media
    """
    # parser_classes = (FileUploadParser, )

    queryset = Media.objects.all()
    serializer_class = MediaCreateSerializer
    # permission_classes = []

    # def put(self, request):
    #     file_obj = request.FILES
    #     print(file_obj)
    #     # do some stuff with uploaded file
    #     return Response(status=204)

    # def perform_create(self, serializer):
    #
    #     return serializer


class MediaViewSet(ModelViewSet):
    """
    This class API view is responsible for creating new media
    """
    queryset = Media.objects.all()
    serializer_class = MediaCreateSerializer
    # parser_classes = (MultiPartParser, FormParser,)
    #
    # def perform_create(self, serializer):
    #     print('file: ', self.request.data.get('file'))
    #     serializer.save(file=self.request.data.get('file'))
