#audio_server/urls.py

from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'song', views.SongViewSet)
router.register(r'audiobook', views.AudiobookViewSet, basename='audiobook')
router.register(r'podcast', views.PodcastViewSet, basename='podcast')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]