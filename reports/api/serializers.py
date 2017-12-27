from rest_framework import serializers

from ..models import Report
from media.api.serializers import MediaSerializer
# from witness.api.serializers import WitnessSerializer


class ReportSerializer(serializers.ModelSerializer):
    # media = MediaSerializer(many=True)

    class Meta:
        model = Report
        fields = ['id', 'title', 'message', 'location']


class ReportCreateSerializer(serializers.ModelSerializer):
    # media = MediaSerializer(many=True)

    class Meta:
        model = Report
        fields = ['title', 'message', 'location']


""""""

# class MediaSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Media
#         fields = ['image', 'audio', 'video']
#
#     def validate(self, data):
#         pass
