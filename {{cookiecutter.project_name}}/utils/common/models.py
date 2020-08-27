"""自定义通用模型字段"""

from django.db import models
from django.conf import settings


class OwnerWeightModel(models.Model):
    """用户权重模型虚类"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(verbose_name='权重', default=0)

    class Meta:
        abstract = True
