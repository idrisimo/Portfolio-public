from django.db import models
from django.contrib.auth.models import User

class Vote_system_model(models.Model):
    server_key = models.CharField(max_length=4)
    username = models.ManyToManyField(User)

class Movie_details_model(models.Model):
    movie_id = models.IntegerField()
    movie_name = models.CharField(max_length=100)
    watch_providers = models.CharField(max_length=50)
    release_date = models.DateField()
    movie_overview = models.TextField()
    genre = models.CharField(max_length=50)
    image_link = models.URLField()
    def __str__(self):
        return self.movie_name