from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

class Game(models.Model):
    players = models.ManyToManyField(Player,default=None)

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
        on_delete=models.CASCADE,
    )
    solution = models.OneToOneField(
        Solution,
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
  
