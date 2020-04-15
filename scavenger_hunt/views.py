from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from base.views import IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes as permissions 
from rest_framework.decorators import action
from base.views import IsStaff

from .models import (
 Player, Question, Answer, Problem, Solution, Challenge, Game, Tag
)
from .serializers import (
    PlayerSerializer,
    QuestionSerializer,
    AnswerSerializer,
    ChallengeSerializer,
    GameSerializer,
    ProblemSerializer,
    SolutionSerializer,
)
from rest_framework.response import Response

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
#    permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        player = self.request.user.player
        games = Game.objects.filter(players__id=player.id)
        return games

#    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser|IsStaff])
#    def new_game(self, *args):
#        import ipdb; ipdb.set_trace()
#        game = Game.objects.create(players=Players.objects.all())
#        return game
    @action(detail=False, methods=['post'], permission_classes=[IsAdminUser|IsStaff])
    def new_game(self, request):
        serializer=GameSerializer(data=request.data) 
        serializer.is_valid()
        serializer.save(players=Player.objects.all()) 
        return Response(serializer.data)

    @action(detail=True, methods=['put'], permission_classes=[IsAdminUser|IsStaff])
    def feature(self, request, pk):
        game = Game.objects.get(pk=pk)
        tags = game.tags.filter(category=Tag.Type.featured.value)
        #if game.tags.filter(category=Tag.Type.featured.value):
        if not tags:
            Tag.objects.create(game=game, category=Tag.Type.featured.value)  
        serializer=GameSerializer(game)
        return Response(serializer.data)

#    @permissions([IsAdminUser|IsStaff])
#    def perform_create(self, serializer):
#        serializer.save(players=Player.objects.all())
    def perform_create(self, serializer):
        pass

    def perform_update(self, serializer):
        pass

    def perform_destroy(self, serializer):
        pass

#       import ipdb; ipdb.set_trace()
#        serializer.save(players=Player.objects.all())
#        if not Profile.objects.filter(owner=self.request.user):
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = addres)

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

