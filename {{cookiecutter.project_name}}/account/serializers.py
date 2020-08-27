from account.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器"""
    username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']

    @staticmethod
    def get_username(obj):
        """参考 user.__str__"""
        return str(obj)
