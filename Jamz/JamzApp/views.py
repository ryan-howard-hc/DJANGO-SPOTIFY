from django.shortcuts import render
from rest_framework import viewsets, serializers
from .serializers import ArtistSerializer
from .models import Artist, Genre, Album, Song
from . import serializers
from rest_framework.response import Response

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.GenreSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer