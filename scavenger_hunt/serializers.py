from rest_framework import routers, serializers, viewsets

from .models import Player, Question, Answer, Challenge, Game, Problem, Solution, Tag

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Player
        fields = ('id','user',)

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','text', )

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id','text', )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','category','other_category')

class GameSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = ('id','tags')

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

    class Meta:
        model = Challenge
        fields = ('id','problem','solution')

