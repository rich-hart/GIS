from enum import Enum
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
    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    class Type(Enum):
        featured = "FE"
        @classmethod
        def get_choices(cls):
            choices = [(e.value,e.name) for _,e in enumerate(cls) ]
            return choices

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="tags",
        related_query_name="tag",
    )
    category = models.CharField(
        max_length=2,
        choices=Type.get_choices(),
        null = True,
        blank = True,
        default=None,
    ) 
    other_category = models.CharField(
        max_length=255,
        default=None,
        null = True,
        blank = True,
    )

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
  
