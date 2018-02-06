from rest_framework import serializers

from ..models import Report
from media.api.serializers import MediaSerializer
# from witness.api.serializers import WitnessSerializer


class ReportSerializer(serializers.ModelSerializer):
    media_files = MediaSerializer(many=True)

    class Meta:
        model = Report
        fields = ['id', 'title', 'message', 'location', 'witness', 'media_files']


class ReportCreateSerializer(serializers.ModelSerializer):
    # media = MediaSerializer(many=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Report
        fields = ['id', 'title', 'message', 'location', 'witness']


""""""

# class MediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Media
#         fields = ['image', 'audio', 'video']
#
#     def validate(self, data):
#         pass
