from datetime import timedelta

from utils.env import env

RUN_ENV = env.get('RUN_ENV', 'DEVELOP')

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'utils.drf.pagination.CommonPageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1'],
    'VERSION_PARAM': 'version',
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_RESPONSE_PAYLOAD_HANDLER': 'account.utils.jwt_response_payload_handler',
    'JWT_AUTH_COOKIE': 'JWT'
}
