#views.py
from django.shortcuts import render
from rest_framework import viewsets

from .serializer import SongSerializer
from .serializer import AudiobookSerializer
from .serializer import PodcastSerializer

from .models import Song
from .models import Audiobook
from .models import Podcast
# Create your views here.


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('name_of_song')
    serializer_class = SongSerializer

class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all().order_by('title_of_audiobook')
    serializer_class = AudiobookSerializer

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all().order_by('name_of_podcast')
    serializer_class = PodcastSerializer  