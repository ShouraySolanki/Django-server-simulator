from django.db import models
from datetime import datetime
import uuid

# Create your models here.
class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name_of_song= models.TextField(max_length=100)
    duration=models.IntegerField(null= True)
    upload_time = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
       return self.name_of_song  

class Audiobook(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    title_of_audiobook= models.TextField(max_length=100)
    author_of_title= models.TextField(max_length=100)
    narrator_of_audiobook= models.TextField(max_length=100)
    duration=models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return self.title_of_audiobook

class Podcast(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name_of_podcast= models.TextField(max_length=100)
    host_of_podcast= models.TextField(max_length=100)
    duration=models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return self.name_of_podcast