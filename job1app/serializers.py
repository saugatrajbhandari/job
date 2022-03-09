from .models import Job
from rest_framework import serializers

from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)


class JobSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Job
        fields = '__all__'
