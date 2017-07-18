from django.shortcuts import render
from .serializers import UserSerializer, ProfileSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Profile
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
