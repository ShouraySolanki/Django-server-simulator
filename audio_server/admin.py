from django.contrib import admin
from .models import Song
from .models import Audiobook
from .models import Podcast

# Register your models here.

admin.site.register(Song)
admin.site.register(Audiobook)
admin.site.register(Podcast)