from rest_framework import serializers

from tag.models import ColoredTag


class ColoredTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColoredTag
        fields = ['name', 'color']


class ColoredTagListSerializer(ColoredTagSerializer):
    pass


class ColoredTagSerializerField(serializers.Field):
    def to_internal_value(self, data):
        pass

    def to_representation(self, value):
        return ColoredTagSerializer(value).data
