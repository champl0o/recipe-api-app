from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag mobjects"""

    class Meta:
        model = Tag
        field = ('id', 'name')
        read_only_fields = ('id',)
