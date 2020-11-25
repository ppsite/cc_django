"""
推荐容器化运行，所以不建议日志落盘，直接输出到 stdout 即可；
如果有日志落盘要求，可直接取消如下注释即可；
"""

# import os
# from django.conf import settings

# 格式化日志输出
# LOG_DIR = os.path.join(settings.BASE_DIR, 'logs')
# LOG_CLS = 'logging.handlers.RotatingFileHandler'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s [%(asctime)s] %(pathname)s %(lineno)d %(funcName)s %(process)d %(thread)d \n \t %(message)s \n',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s \n'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        # 'root': {
        #     'class': LOG_CLS,
        #     'formatter': 'verbose',
        #     'filename': os.path.join(LOG_DIR, 'root.log'),
        #     'maxBytes': 1024 * 1024 * 10,
        #     'backupCount': 5
        # },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'root': {
        #     'handlers': ['root', 'console'],
        #     'level': 'INFO',
        #     'propagate': True,
        # },
    }
}
