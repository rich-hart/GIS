from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# Create your views here.
