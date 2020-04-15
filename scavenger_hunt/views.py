from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from base.views import IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import action
from base.views import IsStaff

from .models import Player, Question, Answer, Problem, Solution, Challenge, Game
from .serializers import (
    PlayerSerializer,
    QuestionSerializer,
    AnswerSerializer,
    ChallengeSerializer,
    GameSerializer,
    ProblemSerializer,
    SolutionSerializer,
)


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

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    def get_queryset(self):
        import ipdb; ipdb.set_trace;
        user = self.request.user
        player = Player.objects.get(user=user)
        return player.games

    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser|IsStaff])
    def new_game(self):
        import ipdb; ipdb.set_trace;
        game = Game()
        for player in Player.objects.get():
            game.players.append(player)
        game.save()
        return game

#    def perform_create(self, serializer):
#        pass
#        if not Profile.objects.filter(owner=self.request.user):
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = address)

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    permission_classes = [IsAdminUser]

# Create your views here
class PlayerViewSet(viewsets.ModelViewSet):
#    queryset = Profile.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated, IsOwner]
#    allowed_methods = ['GET','POST',]
#    lookup_field = 'owner' 
    base_name = 'player'

    def perform_create(self, serializer):
        pass

    def perform_update(self, serializer):
        pass
    
    def get_queryset(self):
        user = self.request.user
        return Player.objects.filter(user=user)

