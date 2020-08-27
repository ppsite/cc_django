from django.db.models import Q
from model_utils.models import now
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from demo.serializers import Demo, DemoListSerializer
from utils.constants import STATUS_PUBLISHED
from utils.drf.mixins import MultiSerializersMixin


# Create your views here.


class DemoViewSets(MultiSerializersMixin, ListModelMixin, GenericViewSet):
    queryset = Demo.objects \
        .filter(is_removed=False, status=STATUS_PUBLISHED) \
        .filter(Q(start__isnull=True) | Q(end__isnull=True) | Q(start__lte=now) | Q(end__gte=now)) \
        .filter(~Q(start__gt=now)).filter(~Q(end__lt=now))
    serializer_class_mapping = {
        'list': DemoListSerializer
    }
