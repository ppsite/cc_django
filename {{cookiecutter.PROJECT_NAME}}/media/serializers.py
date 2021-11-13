from rest_framework import serializers
from media.models import ExternalImage


class ExternalImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalImage
        fields = ['id', 'image', 'created', 'modified']
