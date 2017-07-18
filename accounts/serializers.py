
from django.conf.urls import url, include
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from tribbles.models import Tribble
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from tribbles.views import TribbleViewSet
from .models import Profile
# Serializers define the API representation.

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', )

