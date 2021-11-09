from django.db.models import Q
from model_utils.models import now
from rest_framework.filters import BaseFilterBackend


class OwnerFilter(BaseFilterBackend):
    """过滤属于当前用户的数据"""

    def filter_queryset(self, request, queryset, view):
        current = request.user
        return queryset.filter(owner=current)


class TimeRangeFilter(BaseFilterBackend):
    """时间区间过滤器"""

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(
            Q(start__isnull=True) | Q(end__isnull=True) | Q(start__lte=now) | Q(end__gte=now)).filter(
            ~Q(start__gt=now)).filter(~Q(end__lt=now))
