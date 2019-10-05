from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=150)
    tmd_id = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    overview = models.TextField()
    production_company = models.CharField(max_length=50)
    homepage = models.CharField(max_length=150)
    release_date = models.CharField(max_length=50)
    backdrop_path = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Score(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()

   
