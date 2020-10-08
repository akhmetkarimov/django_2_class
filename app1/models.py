from django.db import models

# Create your models here.

class MyModel(models.Model):
    color = models.CharField(max_length=255)
    speed = models.PositiveIntegerField()
    model = models.CharField(max_length=255)