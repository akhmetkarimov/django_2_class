from django.db import models

# Create your models here.

class MyModel(models.Model):
    color = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()
    model = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, default='')

class Account(models.Model):
    account_username = models.CharField(max_length=255, unique=True)
    account_description = models.TextField()
    account_followers = models.IntegerField()
    account_following = models.IntegerField()
    account_posts = models.IntegerField()

