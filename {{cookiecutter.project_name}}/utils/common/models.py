"""自定义通用模型字段"""

from django.db import models
from uuid import uuid4
from django.conf import settings


class UUIDModel(models.Model):
    """uuid without - """
    id = models.CharField(verbose_name='id', max_length=32, default=uuid4().hex, primary_key=True, unique=True)

    class Meta:
        abstract = True


class OwnerWeightModel(models.Model):
    """用户权重模型虚类"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)
    weight = models.PositiveSmallIntegerField(verbose_name='权重', default=0)

    class Meta:
        abstract = True
