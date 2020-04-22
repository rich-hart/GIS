from enum import Enum
from django.db import models
from django.contrib.auth.models import User

from base.models import Base, Tag
# Create your models here.


class Player(Base):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

class Game(Base):
    players = models.ManyToManyField(Player)

class Problem(Base):
    pass

class Solution(Base):
    pass

class Question(Problem):
    text = models.TextField()

class Answer(Solution):
    text = models.TextField()

class Challenge(Base):
    problem = models.OneToOneField(
        Problem,
        on_delete=models.CASCADE,
    )
    solution = models.OneToOneField(
        Solution,
        on_delete=models.CASCADE,
    )
    game = models.ForeignKey(Game, related_name='challenges', on_delete=models.CASCADE,default=None,null=True,blank=True)
    index = models.IntegerField(default=1)

    class Meta:
        ordering = ['index','id']

class Achievement(Base):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
#        related_name='player_achievements',
#        related_query_name='player_achievements',
    )
    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.DO_NOTHING,
    )
    verified = models.DateTimeField(default=None,null=True,blank=True)

class Penalty(Base):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

