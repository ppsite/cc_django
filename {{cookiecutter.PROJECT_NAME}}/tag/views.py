from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from tag.serializers import ColoredTagSerializer
from tag.models import ColoredTag


class ColoredTagViewSets(ListModelMixin, CreateModelMixin, GenericViewSet):
    """项目视图"""
    queryset = ColoredTag.objects.all()
    serializer_class = ColoredTagSerializer
    filterset_fields = ['content_type', 'object_id']
