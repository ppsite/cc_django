from django.contrib.auth.models import Group
from account.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器"""

    class Meta:
        model = User
        fields = ['id', 'name', 'cn_name', 'name', 'avatar', 'wx', 'mobile']


class GroupSerializer(serializers.ModelSerializer):
    """用户组序列化器"""

    class Meta:
        model = Group
        fields = "__all__"


class UserRetrieveSerializer(UserListSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    access = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'avatar', 'email', 'wx', 'qq', 'mobile', 'access', 'groups']

    @staticmethod
    def get_access(obj):
        """获取用户权限，ant design pro 直接使用使用 access 单数，此处不再修改"""
        return obj.get_all_permissions()
