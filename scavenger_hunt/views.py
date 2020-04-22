import re
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
    


