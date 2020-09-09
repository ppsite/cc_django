"""添加各环境公用配置"""
from utils.env import os, Env
{%- if cookiecutter.use_grappelli.lower() == 'y' %}
from config.common.grappelli.config import *
from config.common.filebrowser import *
{%- endif %}
{%- if cookiecutter.use_drf.lower() == 'y' %}
from config.common.drf import *
{%- endif %}
{%- if cookiecutter.use_celery.lower() == 'y' %}
from config.common.celery import *
{%- endif %}
{%- if cookiecutter.use_mdeditor.lower() == 'y' %}
from config.common.mdeditor import *
{%- endif %}
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
    {%- if cookiecutter.use_grappelli.lower() == 'y' %}
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    {%- endif %}
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS += [
    # 第三方依赖项目
    {%- if cookiecutter.use_taggit.lower() == 'y' %}
    'taggit',
    'taggit_serializer',
    {%- endif %}
    {%- if cookiecutter.use_drf.lower() == 'y' %}
    'rest_framework',
    'rest_framework_jwt',
    {%- endif %}
    {%- if cookiecutter.use_celery.lower() == 'y' %}
    'django_celery_beat',
    {%- endif %}
    {%- if cookiecutter.use_grappelli.lower() == 'y' %}
    'django.contrib.sites',
    {%- endif %}
]

INSTALLED_APPS += [
    # 自研应用
    {%- if cookiecutter.use_account.lower() == 'y' %}
    'account.apps.AccountConfig',
    {%- endif %}
]

SECRET_KEY = env.get('SECRET_KEY')

{%- if cookiecutter.use_grappelli.lower() == 'y' %}
SITE_ID = 1
{%- endif %}

{%- if cookiecutter.use_account.lower() == 'y' %}
# 自定义用户模型
AUTH_USER_MODEL = 'account.User'
{%- endif %}

# 静态资源路径
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

# media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
