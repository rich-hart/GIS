from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Ticket
class RaffleTests(APITestCase):
    def test_single_purchase(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('purchase-list')
        data = {
            'item': '1X',
               
                    "email": "u@d.com",
                    "first_name": "first",
                    "last_name": "last",
               
        }
        old_ticket_total = Ticket.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(),old_ticket_total+1)

    def test_five_purchase(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('purchase-list')
        data = {
            'item': '5X', 
            "email": "u@d.com",
            "first_name": "first",
            "last_name": "last",
                
        }
        old_ticket_total = Ticket.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(),old_ticket_total+5)

    def test_ten_purchase(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('purchase-list')
        data = {
            'item': '10X',
            
                "email": "u@d.com",
                "first_name": "first",
                "last_name": "last",
            
        }
        old_ticket_total = Ticket.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(),old_ticket_total+10)

# Create your tests here.
