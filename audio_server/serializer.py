#serializer.py

from rest_framework import serializers
from .models import Song
from .models import Audiobook
from .models import Podcast

class SongSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Song
        fields = ('id','name_of_song',  'duration', 'upload_time')

class AudiobookSerializer(serializers.HyperlinkedModelSerializer):
      
    class Meta:
        model = Audiobook
        fields = ('id','title_of_audiobook', 'author_of_title', 'narrator_of_audiobook', 'duration', 'upload_time')

class PodcastSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Podcast
        fields = ('id','name_of_podcast', 'host_of_podcast', 'duration', 'upload_time')