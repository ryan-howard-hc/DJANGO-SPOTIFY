from django.db import models

class Artist(models.Model):
    id = models.AutoField                   #Autofield auto generates unique integer value
    name = models.CharField(max_length=100)
                                            #Manager is an class that provides interface for querying the db
                                            # queries like filter,exclude, get
class Album(models.Model):
    id = models.AutoField
    label = models.CharField(max_length=100)
    

class Genre(models.Model):
    id = models.AutoField
    label = models.CharField(max_length=100)
    
    
class Song(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    