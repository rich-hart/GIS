from enum import Enum
from django.db import models
from django.contrib.auth.models import User

from gis.storage_backends import MediaStorage, StaticStorage
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
    video = models.FileField(storage=MediaStorage(),default=None,null=True,blank=True)
    picture = models.FileField(storage=MediaStorage(),default=None,null=True,blank=True)

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
        permissions = [
            ("access_challenge", "Can access the challenge"),
        ]

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

class Reward(Base):
    class Type(Enum):
        general = 'general'
        clue = 'clue'
        praise = 'praise'
        points = 'points'
        key = 'key'
        powers = 'powers'
        promotion = 'promotion'
        completion = 'completion'
        media = 'media'
        @classmethod
        def get_choices(cls):
            return [ (name,value) for (name,value) in enumerate(cls) ]

    challenge = models.ForeignKey(
        Challenge,
        on_delete=models.DO_NOTHING,
    )
    category = models.CharField(
        max_length=127,
        default = Type.general.value,
        choices=Type.get_choices(),
    )
    description = models.TextField()
    unique = models.BooleanField(default=False)
    class Meta:
        ordering = ['-created']
        permissions = [
            ("access_reward", "Can access the reward"),
        ]

class Award(Base):
    player = models.ForeignKey(
        Player,
        on_delete=models.DO_NOTHING,
    )
    reward = models.ForeignKey(
        Reward,
        on_delete=models.DO_NOTHING,
    )
    class Meta:
        ordering = ['-created']


class Penalty(Base):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        null=True,
    )
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)

class PenaltyTag(Base):
    class Type(Enum):
        yellow = 'yellow'
        red = 'red'
        general = 'general'
        @classmethod
        def get_choices(cls):
            return [ (name,value) for (name,value) in enumerate(cls) ]
    instance = models.ForeignKey(
        Penalty,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    name = models.CharField(
        max_length=127,
        default = Type.general.value,
        choices=Type.get_choices(),
    )
    description = models.TextField()
    class Meta:
        ordering = ['-created']
