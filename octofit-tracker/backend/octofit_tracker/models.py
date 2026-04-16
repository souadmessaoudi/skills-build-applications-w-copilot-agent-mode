from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
    def __str__(self):
        return f"{self.user_email} - {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
