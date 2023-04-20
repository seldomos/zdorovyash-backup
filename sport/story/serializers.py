from .models import Story
from rest_framework import serializers


class StorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Story
        fields = ['pk', 'heading', 'description']
