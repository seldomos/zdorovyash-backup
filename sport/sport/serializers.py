from .models import SportItem, Season
from rest_framework import serializers


class SportItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SportItem
        fields = ['pk', 'title', 'image'] # ignore: season and description


class SeasonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Season
        fields = ['pk', 'season']
