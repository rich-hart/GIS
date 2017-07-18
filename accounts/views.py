from django.shortcuts import render
from .serializers import (UserSerializer, ProfileSerializer, AddressSerializer
,AccountSerializer)
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Profile
from address.models import Address
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    basename = 'accounts'

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        



