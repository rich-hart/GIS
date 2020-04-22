import re
from datetime import timedelta, datetime
#import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend

from django.utils import timezone
from fuzzywuzzy import fuzz
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from base.views import IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes as permissions 
from rest_framework.decorators import action
from base.views import IsStaff
from rest_framework.response import Response
from rest_framework import permissions

from .models import * 
from .serializers import *

class IsUnlocked(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True

class IsAvatar(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
#        import ipdb; ipdb.set_trace()
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
#        if request.method in permissions.SAFE_METHODS:
#            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user.player

class IsPlayer(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
#        import ipdb; ipdb.set_trace()
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
#        if request.method in permissions.SAFE_METHODS:
#            return True

        # Write permissions are only allowed to the owner of the snippet.
        return request.user.player


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAdminUser]

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [IsAdminUser]

class SolutionViewSet(viewsets.ModelViewSet):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer
    permission_classes = [IsAdminUser]

#class ChallengeViewSet(viewsets.ModelViewSet):
#    queryset = Challenge.objects.all()
#    serializer_class = ChallengeSerializer
#    permission_classes = [IsAdminUser]
class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAdminUser,IsStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game']
#    @action(detail=True, methods=['put'])
#    def solve(self, request, pk):
#        response = {}
#        challenge = Challenge.objects.get(pk=pk)
#        answer = clean_answer(challenge.solution.answer.text)
#        player_answer = clean_answer(request.data.get('answer',''))
#        if fuzz.ratio(answer,player_answer) > 94:
#            (achievement, created) = Achievement.objects.get_or_create(player=request.user.player,challenge=challenge)
#            if created:
#                achievement.verified = timezone.now()
#                achievement.save()
#            response['message']="Solution correct!"
#        else:
#            #penalty
#            response['message']="Solution incorrect!"
#        return Response(response)

#    def perform_create(self, serializer):
#        pass
#
#    def perform_update(self, serializer):
#        pass
#
#    def perform_destroy(self, serializer):
#        pass
#
#    def get_queryset(self):
#
#        game_query = self.request.user.player.game_set.all()
#        challenge_query = Challenge.objects.filter(game_id__in=game_query.all().values('id'))
#        return challenge_query


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
#    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdminUser,IsStaff]

#    def get_queryset(self):
#        player = self.request.user.player
#        games = Game.objects.filter(players__id=player.id)
#        return games

#    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser|IsStaff])
#    def new_game(self, *args):
#        import ipdb; ipdb.set_trace()
#        game = Game.objects.create(players=Players.objects.all())
#        return game
#    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser|IsStaff])
#    def new_game(self, request):
#        serializer=GameSerializer(data=request.data) 
#        serializer.is_valid()
#        serializer.save(players=Player.objects.all()) 
#        return Response(serializer.data)
    #FIXME: Need Player and Challenge pemission classes
#    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
#    def next_challenge(self, request, pk):
#        completed_challenges = Achievement.objects.filter(player=request.user.player).values('challenge')
#        challenges = Challenge.objects.filter(game__id=pk)
#        remaining_challenges = challenges.exclude(pk__in=completed_challenges.values('pk'))
#        next_challenge = remaining_challenges.order_by('index').first()
#        serializer = ChallengeSerializer(next_challenge)
#        data = serializer.data
#        data.pop('solution',None)
#        return Response(data)


#    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser|IsStaff])
#    def feature(self, request, pk):
#        game = Game.objects.get(pk=pk)
#        tags = game.tags.filter(category=Tag.Type.featured.value)
#        #if game.tags.filter(category=Tag.Type.featured.value):
#        if not tags:
#            Tag.objects.create(game=game, category=Tag.Type.featured.value)  
#        serializer=GameSerializer(game)
#        return Response(serializer.data)

#    @permissions([IsAdminUser|IsStaff])
#    def perform_create(self, serializer):
#        serializer.save(players=Player.objects.all())
#    def perform_create(self, serializer):
#        pass
#
#    def perform_update(self, serializer):
#        pass
#
#    def perform_destroy(self, serializer):
#        pass

#       import ipdb; ipdb.set_trace()
#        serializer.save(players=Player.objects.all())
#        if not Profile.objects.filter(owner=self.request.user):
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = addres)
def clean_answer(text):
    if text:
        text = re.sub('[^a-z]+', '',text.lower())
    return text

#class ChallengeViewSet(viewsets.ModelViewSet):
#    queryset = Challenge.objects.all()
#    serializer_class = ChallengeSerializer
#    permission_classes = [IsAuthenticated,IsUnlocked]
#    filter_backends = [DjangoFilterBackend]
#    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
#        pass
#    @action(detail=True, methods=['put'])
#    def solve(self, request, pk):
#        response = {}
#        challenge = Challenge.objects.get(pk=pk)
#        answer = clean_answer(challenge.solution.answer.text)
#        player_answer = clean_answer(request.data.get('answer',''))
#        if fuzz.ratio(answer,player_answer) > 94:
#            (achievement, created) = Achievement.objects.get_or_create(player=request.user.player,challenge=challenge)
#            if created:
#                achievement.verified = timezone.now()
#                achievement.save()
#            response['message']="Solution correct!"
#        else:
#            #penalty
#            response['message']="Solution incorrect!"
#        return Response(response)

#    def perform_create(self, serializer):
#        pass
#
#    def perform_update(self, serializer):
#        pass
#
#    def perform_destroy(self, serializer):
#        pass
#
#    def get_queryset(self):
#
#        game_query = self.request.user.player.game_set.all()
#        challenge_query = Challenge.objects.filter(game_id__in=game_query.all().values('id'))
#        return challenge_query

# Create your views here
class HiddenChallengeViewSet(viewsets.ModelViewSet):
    serializer_class = HiddenChallengeSerializer
    permission_classes = [IsAuthenticated,IsPlayer]
    base_name = 'hidden_challenge'

    def perform_create(self, serializer):
        pass

    def perform_update(self, serializer):
        pass

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated,IsPlayer])
    def solve(self, request, pk):
        response = {'alert':None}
        challenge = Challenge.objects.get(pk=pk)
        game = challenge.game
        cooldown = timedelta(minutes=5)

        player = request.user.player

#        previous_penalties = Penalty.objects.filter(player=player,game=game,created__gte=datetime.now()-cooldown)
        query_params = {
            'player': player,
            'game': game,
            'created__gte': datetime.now()-cooldown,
            'tag__name': 'red',
        }
        penalties = Penalty.objects.filter(**query_params)
        if penalties:
            response['alert'] = 'red'
            cooldown_ends = penalties.first().created+cooldown
            cooldown_ends_str = cooldown_ends.strftime("%H:%M:%S")
            description = f"Red alert ends at {cooldown_ends_str}"
            response['description'] = description
            return Response(response)
        player_answer_text = request.data.get('answer')

        player_answer_text = clean_answer(player_answer_text)

        solution_answer_text = challenge.solution.answer.text
        if fuzz.ratio(player_answer_text, solution_answer_text) > 94:
            (achievement, created) = Achievement.objects.get_or_create(player=player,challenge=challenge)
            if created:
                achievement.verified = timezone.now()
                achievement.save()
            response['message']="Solution correct!"
        else:

            query_params = {
                'player': player,
                'game': game,
                'created__gte': datetime.now()-cooldown,
                'tag__name': 'yellow',
            }
            yellow_penalties = Penalty.objects.filter(**query_params)
            query_params = {
                'player': player,
                'game': game,
                'created__gte': datetime.now()-cooldown,
                'tag__name': 'general',
            }
            general_penalties = Penalty.objects.filter(**query_params)
            penalty = Penalty.objects.create(player=player, game=game)

            if yellow_penalties:
                tag_type = PenaltyTag.Type.red.value
                cooldown_ends = datetime.now()+cooldown
                cooldown_ends_str = cooldown_ends.strftime("%H:%M:%S")
                description = f"Red alert ends at {cooldown_ends_str}"
                penalty_tag =  PenaltyTag.objects.create(instance=penalty, name=tag_type)
                response['alert'] = 'red'
                response['description'] = description
            elif general_penalties:
#                penalty = Penalty.objects.create(player=player, game=game)
                tag_type = PenaltyTag.Type.yellow.value
                penalty_tag =  PenaltyTag.objects.create(instance=penalty, name=tag_type)
                response['alert'] = 'yellow'
            else:
                tag_type = PenaltyTag.Type.general.value
                penalty_tag =  PenaltyTag.objects.create(instance=penalty, name=tag_type)
                response['alert'] = 'general'

            #penalty_tag = PenaltyTag.objects.create(penalty, name=PenaltyTag.Type.general.value)
            response['message']="Solution incorrect!"
            response['penalty'] = {'created': penalty.created}
        return Response(response)
            #penalty
#            response['message']="Solution incorrect!"
#        return Response({'message':"Solution incorrect!"})
#        pass
#        answer = clean_answer(challenge.solution.answer.text)
#        player_answer = clean_answer(request.data.get('answer',''))
#        if fuzz.ratio(answer,player_answer) > 94:
#            (achievement, created) = Achievement.objects.get_or_create(player=request.user.player,challenge=challenge)
#            if created:
#                achievement.verified = timezone.now()
#                achievement.save()
#            response['message']="Solution correct!"
#        else:
#            #penalty
#            response['message']="Solution incorrect!"
#        return Response(response)


    def perform_destroy(self, serializer):
        pass
#    @action(detail=True, methods=['get','post'], permission_classes=[IsAuthenticated,IsPlayer])
#    def solve(self, request, pk=None):
##        import ipdb; ipdb.set_trace()
#        serializer = ChallengeSerializer(data={})
#        serializer.is_valid()
#        return Response(serializer.data)

    def get_queryset(self):
        game_query = self.request.user.player.game_set.all()
        challenge_query = Challenge.objects.filter(game_id__in=game_query.all())
        return challenge_query
    
class AvatarViewSet(viewsets.ModelViewSet):
#    queryset = Player.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAuthenticated,IsAvatar]
    base_name = 'avatar'

    def perform_create(self, serializer):
        pass

    def get_queryset(self):
        user = self.request.user
        return Player.objects.filter(user=user)



    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated,IsAvatar])
    def challenges(self, request, pk):
#        import ipdb; ipdb.set_trace()
        game_pk=request.query_params.get('game')
        data = []
        player = request.user.player
        if game_pk:
            games = player.game_set.filter(pk=game_pk)
        else:
            games =  player.game_set.all()

        #game_pks = games.values_list(flat=True)
        game_pks = games.values_list('pk',flat=True)  
        challenges = Challenge.objects.filter(game_id__in = game_pks)
        completed_challenges = Achievement.objects.filter(player=request.user.player).values('challenge')

#        completed_serializer = ChallengeSerializer(completed_challenges,many=True)
#        completed_data = completed_serializer.data
        completed_challenges = challenges.filter(pk__in=completed_challenges.values('pk'))
        completed_serializer = ChallengeSerializer(completed_challenges,many=True)
        completed_data = completed_serializer.data
        remaining_challenges = challenges.exclude(pk__in=completed_challenges.values('pk'))
        remaining_serializer = HiddenChallengeSerializer(remaining_challenges,many=True)
        remaining_data = remaining_serializer.data
#        [ challenge_data.pop('solution',None) for challenge_data in remaining_data ] 
#            challenge_data.pop('solution')
#        data = {}
#        serializer =  ChallengeSerializer(challenges,many=True)
        data = completed_data + remaining_data
        return Response(data)
#    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated,IsAvatar])
#    def game(self, request, pk):
#        import ipdb; ipdb.set_trace()
#        data = {}
#        return Response(data)
#        completed_challenges = Achievement.objects.filter(player=request.user.player).values('challenge')
#        challenges = Challenge.objects.filter(game__id=pk)
#        remaining_challenges = challenges.exclude(pk__in=completed_challenges.values('pk'))
#        next_challenge = remaining_challenges.order_by('index').first()
#        serializer = ChallengeSerializer(next_challenge)
#        data = serializer.data
#        data.pop('solution',None)
#        return Response(data)



class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [
        #IsAuthenticated,
        IsStaff,
        IsAdminUser,
    #IsOwner
    #
    ]
#    allowed_methods = ['GET','POST',]
#    lookup_field = 'owner' 
    base_name = 'player'

#    def get_queryset(self):
#        return Player.objects.all()
#    @action(detail=False, methods=['put'])
#    def join_featured_game(self, request):
#        player = request.user.player
#        current_featured_game = Game.objects.filter(tag__category=Tag.Type.featured.value).first()
#        if not current_featured_game.players.filter(pk=player.pk).exists():
#            current_featured_game.players.add(player)
#            current_featured_game.save()
#        serializer=PlayerSerializer(player)
#        return Response(serializer.data)
#
#    def perform_create(self, serializer):
#        pass
#
#    def perform_update(self, serializer):
#        pass
#    
#    def get_queryset(self):
#        user = self.request.user
#        return Player.objects.filter(user=user)

# Create your views here
class DemoViewSet(PlayerViewSet):
#    queryset = Profile.objects.all()

    def join_featured_game(self, request):
        player = request.user.player
        if not player:
            return Response({})
        current_featured_game = Game.objects.filter(tag__category=Tag.Type.featured.value).first()
        if not current_featured_game.players.filter(pk=player.pk).exists():
            current_featured_game.players.add(player)
            current_featured_game.save()

        completed_challenges = Achievement.objects.filter(player=request.user.player).values('challenge')
        challenges = Challenge.objects.filter(game__id=current_featured_game.pk)
        remaining_challenges = challenges.exclude(pk__in=completed_challenges.values('pk'))
        next_challenge = remaining_challenges.order_by('index').first()
        serializer = ChallengeSerializer(next_challenge)
        data = serializer.data
        data.pop('solution',None)
        data['answer'] ='Answer here!'
        serializer=PlayerSerializer(player)
        data.update(serializer.data)

        response = {}
        challenge = Challenge.objects.get(pk=next_challenge.pk)
        answer = clean_answer(challenge.solution.answer.text)
        player_answer = clean_answer(request.data.get('answer',''))
        if fuzz.ratio(answer,player_answer) > 94:
            (achievement, created) = Achievement.objects.get_or_create(player=request.user.player,challenge=challenge)
            if created:
                achievement.verified = timezone.now()
                achievement.save()
            response['message']="Solution correct!"
        else:
            #penalty
            response['message']="Solution incorrect!"
        response.update(data)
        return Response(response)
    


