from django.shortcuts import render
from .serializer import (
    PurchaserSerializer,
    PurchaseSerializer, 
    TicketSerializer,
    PrizeSerializer,
)
from rest_framework import viewsets
from .models import Purchaser, Ticket, Purchase, Prize

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class IsStaff(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
#        import ipdb; ipdb.set_trace()
        return request.user.is_staff

class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer 


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer 
    permission_classes = [IsStaff,IsAuthenticated]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class PrizeViewSet(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer

