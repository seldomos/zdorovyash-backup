from django.shortcuts import render
from rest_framework import viewsets
from .models import SportItem, Season
from .serializers import SportItemsSerializer, SeasonSerializer


class SportItemViewSet(viewsets.ModelViewSet):
    queryset = SportItem.objects.all()
    serializer_class = SportItemsSerializer


class SeasonsViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer
