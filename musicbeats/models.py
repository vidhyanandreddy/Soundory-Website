from django.db import models
from django.contrib.auth.models import User

# vidhyanand vidhyanand067@gmail.com 1234
# Create your models here.

################   Songs_Model   #################
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    song = models.FileField(upload_to='songs/')
    movie = models.CharField(max_length=1000,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

###################   Podcast_Model   #################
class Podcast(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    audio = models.FileField(upload_to='songs/')
    creator = models.CharField(max_length=50)
    def __str__(self):
        return self.title

##################   WatchLater_Model   ########################
class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    video_id =models.CharField(max_length=10000000, default="")
  
######################   Liked_Model   ########################
class liked(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    video_id =models.CharField(max_length=10000000, default="")
   
###################   History_Model   ########################### 
class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=10000000, default="")

##################   Channel_Model   #####################
class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    music = models.CharField(max_length=100000000)