from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from base.views import IsOwner
from rest_framework.permissions import IsAdminUser,IsAuthenticated

from .models import Player, Question, Answer
from .serializers import (
    PlayerSerializer,
    QuestionSerializer,
    AnswerSerializer
)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
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
#        if not Profile.objects.filter(owner=self.request.user):
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = address)

    def perform_update(self, serializer):
        pass
#        import ipdb; ipdb.set_trace()
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = address)

    
    def get_queryset(self):
        user = self.request.user
        return Player.objects.filter(user=user)

