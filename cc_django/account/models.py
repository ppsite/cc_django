from django.db import models
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import AbstractUser
from model_utils.models import SoftDeletableModel, UUIDModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager
from account.avatar import IDAvatar


class AnonymousAccount(AnonymousUser):
    avatar = 'http://www.gravatar.com/avatar/bf5c77ba8067db6121b6f02d87674dcd?s=80&d=wavatar'

    def __str__(self):
        return '大佬，快来登录哟!'

    def save(self):
        pass

    def delete(self):
        pass

    def set_password(self, raw_password):
        pass

    def check_password(self, raw_password):
        pass


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **kwargs):
        if not email:
            raise ValueError('email 必须提供')
        user = self.model(email=email,
                          password=make_password(password=password),
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          **kwargs)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **kwargs):
        pwd = password or "123"
        return self._create_user(email=email, password=pwd, is_staff=False, is_superuser=False, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        return self._create_user(email=email, password=password, is_staff=True, is_superuser=True, **kwargs)


class User(UUIDModel, SoftDeletableModel, AbstractUser):
    """自定义用户模型"""
    # 必填字段
    email = models.EmailField(verbose_name='邮箱', max_length=25, unique=True)
    mobile = models.CharField(verbose_name='手机', max_length=11, blank=True, null=True)

    # 选填字段
    username = models.CharField(verbose_name='用户', max_length=20, blank=True)
    avatar = models.CharField(verbose_name='头像', default=IDAvatar(email).wavatar(), max_length=200)
    qq = models.CharField(verbose_name='QQ号', max_length=32, blank=True, null=True)
    wx = models.CharField(verbose_name='微信', max_length=32, blank=True, null=True)

    # 额外用户状态字段，根据不同项目调整

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = verbose_name = '自定义用户'

    def __str__(self) -> str:
        if self.first_name and self.last_name:
            return '%s%s' % (self.last_name, self.first_name)
        else:
            return str(self.email).split('@')[0]

    def save(self, *args, **kwargs) -> None:
        super(User, self).save(*args, **kwargs)
        if not self.username:
            self.username = str(self.email).split('@')[0]
