from django.shortcuts import render
from .serializers import (UserSerializer, ProfileSerializer, AddressSerializer
,AccountSerializer)
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Profile
from address.models import Address

from rest_framework import permissions


class IsOwner(permissions.BasePermission):
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
        return obj.owner == request.user

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAdminUser]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    allowed_methods = ['GET']
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'owner'
    base_name = 'account'
    allowed_methods = ['GET']
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,IsOwner]
    allowed_methods = ['GET','POST']
#    lookup_field = 'owner' 
    base_name = 'profile'
    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
        if not Profile.objects.filter(owner=self.request.user):
            address = Address(raw = self.request.data['address'])
            address.save()
            serializer.save(owner=self.request.user, address = address)
        
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)


