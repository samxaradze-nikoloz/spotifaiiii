from django.db import models
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100 , default='Unknown')
    popularity = models.IntegerField(default=0)  
    followers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    total_tracks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=200)
    duration_seconds = models.PositiveIntegerField( default=0)  
    track_number = models.PositiveIntegerField(default=1)
    explicit = models.BooleanField(default=False)
    popularity = models.IntegerField(default=0)  

    def __str__(self):
        return self.title



# Create your models here.


