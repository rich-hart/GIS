from django.shortcuts import render
from .serializer import (
    PurchaserSerializer,
    PurchaseSerializer, 
    TicketSerializer
)
from rest_framework import viewsets
from .models import Purchaser, Ticket, Purchase 

class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer 


class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer 

    def perform_create(self, serializer):
#        import ipdb; ipdb.set_trace()
#        serializer.save()
        data = serializer.data
        purchaser = Purchaser(
            email=data['email'],
            first_name = data['first_name'],
            last_name = data['last_name'],
        )
        purchaser.save()
        purchase = Purchase(
            item = data['item'],
            buyer = purchaser
        )
        purchase.save()
        units = 0
        if data['item']=='1X':
            units = 1
        elif data['item']=='5X':
            units = 5
        elif data['item']=='10X':
            units = 10
        else:
            #RAISE ERROR
            units = 0
        for i in range(0, units):
            ticket = Ticket(owner = purchaser)
            ticket.save()
        

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

