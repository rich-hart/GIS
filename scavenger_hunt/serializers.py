from rest_framework import routers, serializers, viewsets

from .models import *

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

class PlayerSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    game_set = GameSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = ('id','user','game_set')


class ProblemSerializer(serializers.HyperlinkedModelSerializer):
    question = QuestionSerializer()
    class Meta:
        model = Problem
        fields = ('id','question')

class SolutionSerializer(serializers.HyperlinkedModelSerializer):
    answer = AnswerSerializer()
    class Meta:
        model = Solution
        fields = ('id','answer')



class ChallengeSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    #solution = SolutionSerializer()
    #solution = serializers.HiddenField(default="ANSWER")

    class Meta:
        model = Challenge
        fields = ('id','problem',)
        read_only_fields = ('id', 'problem',)
#        extra_kwargs = {
#            'solution': {'write_only': True},
#        }
class AchievementSerializer(serializers.ModelSerializer):
    player = PlayerSerializer()
    challenge = ChallengeSerializer()

    class Meta:
        model = Challenge
        fields = ('id','player','challenge')
        read_only_fields = ('id', 'player','challenge')

