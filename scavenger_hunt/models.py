from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
     pass

class Player(models.Model):
    user = models.OneToOneField(
        User,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Problem(models.Model):
    pass

class Solution(models.Model):
    pass

class Question(Problem):
    text = models.TextField()

class Answer(Solution):
    text = models.TextField()

class Challenge(models.Model):
    problem = models.OneToOneField(
        Problem,
    )
    solution = models.OneToOneField(
        Solution,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
  
