from django.contrib.auth.models import AnonymousUser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from account.serializers import User, UserListSerializer
from utils.drf.mixins import MultiSerializersMixin


class CurrentViewSet(MultiSerializersMixin, ListModelMixin, GenericViewSet):
    """
    前端接口: 获取当前登录用户
    """
    queryset = User.objects.filter(is_active=True, is_removed=False)
    serializer_classes = [UserListSerializer]
    authentication_classes = [JSONWebTokenAuthentication]

    def list(self, request, *args, **kwargs):
        if isinstance(request.user, AnonymousUser):
            return Response()
        else:
            serializer = UserListSerializer(request.user)
            return Response(serializer.data)
