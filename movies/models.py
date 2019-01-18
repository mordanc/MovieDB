from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=64)
    release_date = models.DateField()
    movie_summary = models.CharField(max_length=2048, default="")

    def __str__(self):
        return self.movie_title

class Tag(models.Model):
    movie = models.ManyToManyField(Movie)
    tag_name = models.CharField(max_length=16)
    def __str__(self):
        return self.tag_name

class Actor(models.Model):
    actor_name = models.CharField(max_length=64)
    acted_movies = models.ManyToManyField(Movie)
    def __str__(self):
        return self.actor_name
