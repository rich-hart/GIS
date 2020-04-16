from django.shortcuts import render
from .serializers import (UserSerializer, ProfileSerializer, 
#AddressSerializer,
AccountSerializer,
#GoogleIDSerializer,
)
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from base.views import IsOwner
from .models import Profile
#from .models import Address




#class AddressViewSet(viewsets.ModelViewSet):
#    queryset = Address.objects.all()
#    serializer_class = AddressSerializer
#    permission_classes = [IsAdminUser]

#class GoogleIDViewSet(viewsets.ModelViewSet):
#    queryset = Address.objects.all().order_by('-id')[:50]
#    serializer_class = GoogleIDSerializer



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
#    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated,IsOwner]
#    allowed_methods = ['GET','POST',]
#    lookup_field = 'owner' 
    base_name = 'profile'
#    def perform_create(self, serializer):

#        if not Profile.objects.filter(owner=self.request.user):
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = address)

#    def perform_update(self, serializer):
#        import ipdb; ipdb.set_trace()
#        address = Address(raw = self.request.data['address'])
#        address.save()
#        serializer.save(owner=self.request.user, address = address)

    
    def get_queryset(self):
        user = self.request.user
        return Profile.objects.filter(owner=user)


