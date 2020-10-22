from django.db import models

# Create your models here.

class CarType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name


class MyModel(models.Model):
    color = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()
    model = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, default='')
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE, blank=True, null=True)


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    def __str__(self):
        return self.genre_name

class Movie(models.Model):
    movie_title = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name='movies')
    
    def __str__(self):
        return self.movie_title


class Account(models.Model):
    account_username = models.CharField(max_length=255, unique=True)
    account_description = models.TextField()
    account_followers = models.IntegerField()
    account_following = models.IntegerField()
    account_posts = models.IntegerField()

