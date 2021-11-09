"""自定义通用模型字段"""
import json
from django.db import models
from django.conf import settings
from model_utils.models import TimeFramedModel as MUTimeFramedModel


class OwnerModel(models.Model):
    """用户权重模型虚类"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class EnabledModel(models.Model):
    """

    """
    is_enabled = models.BooleanField(verbose_name='启用', default=False)

    class Meta:
        abstract = True


class DateTimeFramedModel(MUTimeFramedModel):
    """提供 DateTime 时间窗口属性"""

    class Meta:
        abstract = True

    @property
    def is_effective(self) -> bool:
        """
        检测时间窗口是否生效
        @return: bool
        """
        from datetime import datetime

        start = self.start or datetime.now()
        end = self.end or datetime.now()

        if start <= datetime.now() <= end:
            return True
        return False


class TimeFramedModel(models.Model):
    """提供 TimeField 时间窗口"""
    start = models.TimeField(verbose_name='开始', blank=True, null=True)
    end = models.TimeField(verbose_name='结束', blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def is_effective(self) -> bool:
        """
        检测时间窗口是否生效
        @return: bool
        """
        from time import time

        start = self.start or time()
        end = self.end or time()

        if start <= time() <= end:
            return True
        return False


class ExtraModel(models.Model):
    """
    扩展数据的标记
    """
    extra = models.TextField(verbose_name='额外数据', blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def json_extra(self):
        """ JSON格式化extra 数据内容。"""
        return json.loads(self.extra)
