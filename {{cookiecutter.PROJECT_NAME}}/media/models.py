from uuid import uuid4
from django.db import models
from utils.models import UUIDModel, TimeStampedModel, OwnerModel


def get_upload_to(instance, filename):
    ext = filename.split('.')[-1]
    name = '.'.join(filename.split('.')[0: -1])
    return f'images/{instance.owner.username}/{name}_{uuid4().hex}.{ext}'


class ExternalImage(UUIDModel, OwnerModel, TimeStampedModel):
    """外部图片存储"""
    image = models.ImageField(verbose_name="图标", upload_to=get_upload_to)

    class Meta:
        verbose_name_plural = verbose_name = '- 图片管理'

    def __str__(self):
        return self.image.name
