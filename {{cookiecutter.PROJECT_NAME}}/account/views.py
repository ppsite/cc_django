from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from account.serializers import User, UserListSerializer, UserRetrieveSerializer


class AccountViewSet(ListModelMixin, GenericViewSet):
    """用户模型操作"""
    queryset = User.objects.filter(is_active=True, is_removed=False)
    authentication_classes = [JSONWebTokenAuthentication]
    serializer_class = UserListSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'email', 'mobile']

    @action(methods=['GET'], detail=False, url_path='current')
    def get_current_user(self, request, **kwargs):
        serializer = UserRetrieveSerializer(request.user)
        return Response({"data": serializer.data})

    @action(methods=['POST'], detail=False)
    def logout(self, request, *args, **kwargs):
        logout(request)  # 用户登出
        response = HttpResponseRedirect('/')
        response.delete_cookie(key='JWT')
        return response
