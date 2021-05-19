from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase
from .models import Song
from django.urls import reverse, include, path

class SongTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('audio_server/', include('audio_server.urls')),
    ]
    def test_create_song(self):
        
        url = reverse('song-list')
        data = {'name_of_song': 'Tsunami', 'duration': 2231}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.get().name_of_song, 'Tsunami')
        self.assertEqual(Song.objects.get().duration, 2231)

    # url pattern test case
        response = self.client.get(url,data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)        