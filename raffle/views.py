from django.shortcuts import render
from .serializer import (
    PurchaserSerializer,
    PurchaseSerializer, 
    TicketSerializer
)
from rest_framework import viewsets
from .models import Purchaser, Ticket, Purchase 

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


#    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
#        serializer.save()
#        data = serializer.data
#        purchaser = Purchaser(
#            email=data['email'],
#            first_name = data['first_name'],
#            last_name = data['last_name'],
#        )
#        purchaser.save()
#        purchase = Purchase(
#            item = data['item'],
#            buyer = purchaser
#        )
#        purchase.save()
#        units = 0

        

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


