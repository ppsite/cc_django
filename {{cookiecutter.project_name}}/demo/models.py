import os
import hashlib
from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel, SoftDeletableModel, StatusModel, TimeFramedModel
from model_utils.choices import Choices
from account.models import User
from utils.constants import STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE


# Create your models here.

def get_user_upload_path(instance, filename):
    """
    获取用户上传静态资源路径: /upload/admin_admin.com/album/mae2bfc8c06821fd5e5b2f4d808c6bd12.png
    :param instance: 模型实例
    :param filename: 上传文件名
    :return: 文件路径
    """
    ext = filename.split('.').pop()
    user_email = instance.author.email.replace('@', '_')
    md5_filename = "%s.%s" % (hashlib.md5(filename.encode("utf8")).hexdigest(), ext)
    return os.path.join(user_email, 'album', md5_filename)


class Demo(TimeStampedModel, UUIDModel, SoftDeletableModel, StatusModel):
    """示例代码"""
    STATUS = Choices(STATUS_DRAFT, STATUS_PUBLISHED, STATUS_OFFLINE)
    name = models.CharField(verbose_name='名称', max_length=40)
    cover = models.ImageField(verbose_name='封面', upload_to=get_user_upload_path)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '示例代码'

    def __str__(self):
        return self.name
