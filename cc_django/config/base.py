"""添加各环境公用配置"""
from utils.env import os, Env
from config.common.settings import *
from config.common.grappelli.config import *
from config.common.drf import *
from config.common.celery import *
from config.common.mdeditor import *
from config.common.filebrowser import *
from config.common.logging import *

env = Env()

# 语言/时区
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# 允许主机
# todo 生产环境修改为主域名
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    # 第三方依赖项目
    'taggit',
    'taggit_serializer',
    'rest_framework',
    'rest_framework_jwt',
    'django_celery_beat',
    'django.contrib.sites',
]

INSTALLED_APPS += [
    # 自研应用
    'account.apps.AccountConfig',
]
SITE_ID = 1
# 自定义用户模型
AUTH_USER_MODEL = 'account.User'

# 静态资源路径
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
