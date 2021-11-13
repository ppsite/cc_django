from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from utils.models import UUIDModel


class BaseTag(UUIDModel):
    """独立文本标签基类"""
    content_type = models.ForeignKey(ContentType, verbose_name='模型类型', on_delete=models.CASCADE)
    object_id = models.UUIDField(verbose_name="对象 ID")
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        abstract = True


class ColoredTag(BaseTag):
    """带背景色的文本标签"""
    name = models.CharField(verbose_name='标签名称', max_length=20)
    color = models.CharField(verbose_name='背景颜色', max_length=7, default='#111111')

    class Meta:
        verbose_name_plural = verbose_name = '- 色彩标签'

    def __str__(self):
        return self.name


class KeyValueTag(BaseTag):
    """key=value类型的文本标签"""
    key = models.CharField(verbose_name='键', max_length=20)
    value = models.CharField(verbose_name='值', max_length=20)

    class Meta:
        verbose_name_plural = verbose_name = '- 键值标签'

    def __str__(self):
        return f'{self.key}={self.value}'
