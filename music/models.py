from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title



# Create your models here.


