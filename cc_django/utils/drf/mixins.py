"""
DRF Mixin
"""

from utils.drf.exceptions import GetSerializerError


class MultiSerializersMixin(object):
    """
    多序列化器插件
    !! Mixin 加载有序，请首先继承此类
    actions = [create, delete, list retrieve, update, partial_update]
    """
    serializer_classes = []
    action = None

    def get_action(self):
        flag = 'partial'
        return flag if flag in self.action else self.action

    def get_serializer_class(self):
        assert isinstance(self.serializer_classes, list), "'serializer_class' should be Iterable"
        for item in self.serializer_classes:
            if self.get_action() in item.__name__.lower():
                return item
        raise GetSerializerError('no serializer found for action: %s' % self.action)
