from rest_framework.validators import UniqueValidator
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from tribbles.models import Tribble
from rest_framework.response import Response
from tribbles.views import TribbleViewSet
from .models import Profile
#from .models import Address
# Serializers define the API representation.

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

#class AddressSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Address
#        fields = ('raw', )

#class GoogleIDSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Address
#        fields = ('google_id', 'longitude', 'latitude')

#        read_only_fields = fields

# Serializers define the API representation.
#FIXME: Profile Serializer does not validate properly
# user queryset needs to be restricted. 
class ProfileSerializer(serializers.ModelSerializer):
#    owner = serializers.ReadOnlyField(source='user.email')
#    owner = serializers.CurrentUserDefault()
#    user = serializers.CurrentUserDefault()
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
#    address = serializers.CharField()
    class Meta:
        model = Profile
        fields = ('owner', #'address'
        )
        #read_only_fields = ('owner',)

class AccountSerializer(serializers.HyperlinkedModelSerializer):
#    address = serializers.CharField()
    class Meta:
        model = Profile
        fields = ('owner', 'address',)
         
