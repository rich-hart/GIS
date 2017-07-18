from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tribble
from urllib.parse import urljoin
import os
from rest_framework.test import APIRequestFactory
from .serializers import TribbleSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.decorators import detail_route
from django.contrib.auth.models import User, Group
from rest_framework.response import Response


class TribbleViewSet(viewsets.ModelViewSet):
    queryset = Tribble.objects.all()
    serializer_class = TribbleSerializer
    lookup_field = 'key'
    lookup_value_regex = '[0-9a-f]{32}'
    permission_classes=[IsAuthenticated]

    @detail_route()
    def hunt(self, request, key):
        tribble = self.get_object()
        if not tribble.owner:
            tribble.owner = request.user
        if request.user.is_staff:
            tribble.owner = None
        tribble.save()


        serializer = TribbleSerializer(tribble, many=False, context={'request': request})
        return Response([serializer.data])
      

