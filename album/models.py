from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateField(auto_now_add=True)
    RATING_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES, default='1')
    
    
    def __str__(self):
        return self.album_title