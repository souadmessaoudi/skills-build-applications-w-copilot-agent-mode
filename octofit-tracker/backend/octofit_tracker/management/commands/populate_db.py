from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Modèles simples pour MongoDB (pas de migrations nécessaires)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user_email = models.EmailField()
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Nettoyage
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Création des équipes
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Utilisateurs super-héros
        users = [
            {'email': 'ironman@marvel.com', 'username': 'Iron Man', 'team': marvel},
            {'email': 'spiderman@marvel.com', 'username': 'Spider-Man', 'team': marvel},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': dc},
            {'email': 'superman@dc.com', 'username': 'Superman', 'team': dc},
        ]
        for u in users:
            user = User.objects.create_user(email=u['email'], username=u['username'], password='password')
            # Ajout d'une activité
            Activity.objects.create(user_email=u['email'], type='Running', duration=30)
            # Ajout au leaderboard
            Leaderboard.objects.create(user_email=u['email'], points=100)

        # Workouts
        Workout.objects.create(name='Cardio Blast', description='Intense cardio session')
        Workout.objects.create(name='Strength Training', description='Full body strength')

        self.stdout.write(self.style.SUCCESS('octofit_db has been populated with test data.'))
