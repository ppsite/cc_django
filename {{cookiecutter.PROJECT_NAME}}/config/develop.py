from config.base import *

ALLOWED_HOSTS = ['*']

# 生产环境建议
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
