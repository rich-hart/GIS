from rest_framework import routers, serializers, viewsets
from rest_framework.validators import UniqueValidator
from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','text', 'video','picture')

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id','text', )

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name','description')



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



class NewChallengeSerializer(serializers.ModelSerializer):
    solution = SolutionSerializer()
    problem = ProblemSerializer()
#    game = serializers.RelatedField(source='game', read_only=False,queryset=Game.objects.all(),)
#    game_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False)

#    game = GameSerializer()
#    game_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #solution = SolutionSerializer()
    #solution = serializers.HiddenField(default="ANSWER")
    def create(self, validated_data):
#        import ipdb; ipdb.set_trace()
        a_serializer=AnswerSerializer(data=validated_data['solution']['answer']) 
        a_serializer.is_valid()
        answer = a_serializer.save()
        q_serializer=QuestionSerializer(data=validated_data['problem']['question']) 
        q_serializer.is_valid()
        question = q_serializer.save()
        game = validated_data['game']
        challenge = Challenge.objects.create(problem=question,solution=answer,game=game)
        return challenge

    def update(self, validated_data):
#        import ipdb; ipdb.set_trace()
        a_serializer=AnswerSerializer(data=validated_data['solution']['answer']) 
        a_serializer.is_valid()
        answer = a_serializer.save()
        q_serializer=QuestionSerializer(data=validated_data['problem']['question']) 
        q_serializer.is_valid()
        question = q_serializer.save()
        game = validated_data['game']
        challenge = Challenge.objects.get(validated_data['id'])
        challenge.problem=question
        challenge.solution=answer
        challenge.game=game
        challenge.save()
        return challenge


    class Meta:
        model = Challenge
        fields = ('id','problem','solution','game')

class ChallengeSerializer(serializers.ModelSerializer):
    solution = SolutionSerializer()
    problem = ProblemSerializer()
#    game = serializers.RelatedField(source='game', read_only=False,queryset=Game.objects.all(),)
#    game_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False)

#    game = GameSerializer()
#    game_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    #solution = SolutionSerializer()
    #solution = serializers.HiddenField(default="ANSWER")
    def create(self, validated_data):
#        import ipdb; ipdb.set_trace()
        a_serializer=AnswerSerializer(data=validated_data['solution']['answer']) 
        a_serializer.is_valid()
        answer = a_serializer.save()
        q_serializer=QuestionSerializer(data=validated_data['problem']['question']) 
        q_serializer.is_valid()
        question = q_serializer.save()
        game = validated_data['game']
        challenge = Challenge.objects.create(problem=question,solution=answer,game=game)
        return challenge

    def update(self, challenge, validated_data):
#        import ipdb; ipdb.set_trace()
        a_serializer=AnswerSerializer(data=validated_data['solution']['answer']) 
        a_serializer.is_valid()
        answer = a_serializer.save()
        q_serializer=QuestionSerializer(data=validated_data['problem']['question']) 
        q_serializer.is_valid()
        question = q_serializer.save()
        game = validated_data['game']
        challenge.problem=question
        challenge.solution=answer
        challenge.game=game
        challenge.save()
        return challenge


    class Meta:
        model = Challenge
        fields = ('id','problem','solution','game')
#        extra_kwargs = {
#            'solution': {'write_only': True},
#        }

class HiddenChallengeSerializer(serializers.ModelSerializer):
#    solution = SolutionSerializer()
    problem = ProblemSerializer(read_only=True)
    answer = serializers.CharField(default='Enter Access Code',allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Challenge
        fields = ('id','answer','problem')
        read_only_fields = ('problem',)
#        extra_kwargs = {
#            'solution': {'write_only': True},
#        }

class PenaltySerializer(serializers.ModelSerializer):
#    solution = SolutionSerializer()
#    problem = ProblemSerializer(read_only=True)
#    answer = serializers.CharField(default='ANSWER_HERE',allow_blank=False, trim_whitespace=True)

    class Meta:
        model = Challenge
        fields = ('id','created')
        read_only_fields = fields
#        extra_kwargs = {
#            'solution': {'write_only': True},
#        }

class GameSerializer(serializers.ModelSerializer):
#    challenge_set = ChallengeSerializer()
    class Meta:
        model = Game
        fields = (
            'id',
#            'challenge_set',
        )


class AchievementSerializer(serializers.ModelSerializer):
#    player = PlayerSerializer()
#    challenge = ChallengeSerializer()

    class Meta:
        model = Challenge
        fields = ('id',
                #'player',
                #'challenge'
        )
       # read_only_fields = ('id', 'player','challenge')

class DemoSerializer(serializers.ModelSerializer):
    problem = ProblemSerializer()
    answer = serializers.HiddenField(default = 'Enter Access Code')

    class Meta:
        model = Challenge
        fields = ('id','problem','answer')

class PlayerSerializer(serializers.ModelSerializer):
#    user = serializers.HiddenField(
#        default=serializers.CurrentUserDefault()
#    )
#    game_set = GameSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = ('id','user','game_set')

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = ('id','challenge','category','description')


class AwardSerializer(serializers.ModelSerializer):
#    reward = RewardSerializer()
    class Meta:
        model = Award
        fields = ('id','player','reward')
        read_only_fields = fields


class AvatarSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
#        validators=[UniqueValidator(queryset=User.objects.all())],
    )
#    game_set = GameSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        fields = ('id','user','game_set')
#        read_only_fields = ('user',)
        extra_kwargs = {
            'user': {
                'validators': [UniqueValidator(queryset=User.objects.all())],
            }
        }
