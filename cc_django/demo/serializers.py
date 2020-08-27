from rest_framework.serializers import ModelSerializer
from demo.models import Demo
from account.serializers import UserSerializer


class DemoListSerializer(ModelSerializer):
    """示例序列化"""
    author = UserSerializer(read_only=True)

    class Meta:
        model = Demo
        fields = '__all__'

