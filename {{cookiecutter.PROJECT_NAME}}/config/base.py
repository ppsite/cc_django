"""添加各环境公用配置"""
from utils.env import os, env
from config.settings import *
from config.plugins.logging import LOGGING
{%- if cookiecutter.GRAPPELLI.lower() == 'y' %}
from config.plugins.grappelli import *
{%- endif %}
{%- if cookiecutter.DRF.lower() == 'y' %}
from config.plugins.drf import *
{%- endif %}
{%- if cookiecutter.BOTO3.lower() == 'y' %}
from config.plugins.storage import *
{%- endif %}


# 语言/时区
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

# 允许主机
ALLOWED_HOSTS = ['*']

# 默认依赖
INSTALLED_APPS = [
    # django deps
    'django.contrib.contenttypes',
    { %- if cookiecutter.GRAPPELLI.lower() == 'y' %}
    'grappelli.dashboard',
    'grappelli',
    'filebrowser',
    { %- endif %}
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # cc_django deps
    'account',
    'utils'
]

# 用户选项依赖
INSTALLED_APPS += [
    {%- if cookiecutter.DRF.lower() == 'y' %}
    'rest_framework',
    'rest_framework_jwt',
    {%- endif %}
    {%- if cookiecutter.CELERY.lower() == 'y' %}
    'django_celery_beat',
    {%- endif %}
]

# 用户自定义依赖
INSTALLED_APPS += [

]

# 生产环境随机生成
SECRET_KEY = env.get('SECRET_KEY')

SITE_ID = 1

# 自定义用户模型
AUTH_USER_MODEL = 'account.User'

# 静态资源路径
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')

{%- if cookiecutter.CELERY.lower() == 'y' %}
# CELERY 消息队列
CELERY_BROKER_URL = env.get('CELERY_BROKER_URL')
{%- endif %}

{%- if cookiecutter.BOTO3.lower() == 'y' %}
# 默认文件系统
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
{%- endif %}
