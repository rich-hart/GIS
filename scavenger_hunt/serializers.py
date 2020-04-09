from rest_framework import routers, serializers, viewsets

from .models import Player, Question, Answer, Challenge, Game, Problem, Solution

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Player
        fields = ('user',)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', )

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('players',)

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('id',)

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('id',)

class ChallengeSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    solution = SolutionSerializer()
    game = GameSerializer()
    class Meta:
        model = Challenge
        fields = ('problem','solution','game')

