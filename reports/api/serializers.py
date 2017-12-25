from rest_framework import serializers

from ..models import Report
from media.api.serializers import MediaSerializer


class ReportSerializer(serializers.ModelSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = Report
        fields = ['title', 'message', 'location', 'media']


""""""

# class MediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Media
#         fields = ['image', 'audio', 'video']
#
#     def validate(self, data):
#         pass
