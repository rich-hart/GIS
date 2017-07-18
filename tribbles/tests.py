from django.test import TestCase
from django.contrib.auth.models import User, Group
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tribble
from urllib.parse import urljoin
import os
from rest_framework.test import APIRequestFactory
from .serializers import TribbleSerializer
import json


class TribbleTests(APITestCase):
    fixtures = ['tribbles/test_data.yaml']

    def setUp(self): 
        self.key = '7f57da66d6f1469b85d181f331f7c230'
        self.default_url = reverse('tribble-list')
        self.adopt_url = os.path.join(self.default_url,self.key,'adopt')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')
        self.user_link = 'http://'+os.path.join('testserver','api','users',str(self.user.pk)) + '/' 
        self.staff = User.objects.create_user(
            username='staff_user', email='u@d.com', password='password', is_staff=True)

    def test_anonymous_default(self):
        response = self.client.get(self.default_url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

    def test_anonymous_adopt(self):
        response = self.client.get(self.adopt_url, format='json',follow=True)
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )


    def test_user_default(self):
        self.client.login(username='test_user', password='password')

        response = self.client.get(self.default_url, format='json',follow=True)
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":None}]
        )

    def test_user_adopt(self):
        self.client.login(username='test_user', password='password')
        response = self.client.get(self.adopt_url, format='json',follow=True)
        
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":self.user_link}]
        )
        # Make sure second user cannon change this link once set
        self.user = User.objects.create_user(
            username='test_user_2', email='u@d.com', password='password')

        self.client.login(username='test_user_2', password='password')
        response = self.client.get(self.adopt_url, format='json',follow=True)
        
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":self.user_link}]
        )

    def test_staff_default(self):
        self.client.login(username='staff_user', password='password')

        response = self.client.get(self.default_url, format='json',follow=True)
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":None}]
        )

        self.test_user_adopt()
        self.client.login(username='staff_user', password='password')

        response = self.client.get(self.default_url, format='json',follow=True)
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":self.user_link}]
        )

    def test_staff_adopt(self):
        self.test_staff_default()
        response = self.client.get(self.adopt_url, format='json',follow=True)
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":None}]
        )

        response = self.client.get(self.default_url, format='json',follow=True)
        self.assertEqual(
            json.loads(response.content.decode(response.charset)),
            [{"owner":None}]
        )
