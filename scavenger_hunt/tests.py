from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User, Group


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from myproject.apps.core.models import Account
#from selenium import webdriver
from django.test import LiveServerTestCase
import shutil
import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import urllib


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory

from .models import *
from .pipeline import create_player

class PlayerTests(APITestCase):
    def setUp(self): 
#        import ipdb; ipdb.set_trace()
        self.url = reverse('player-list')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')
        self.users = [
            User.objects.create_user(
                username='test_user_' + str(i),
                email='u@d.com',
                password='password'
            ) for i in range(5)
        ]

    def tearDown(self):
        User.objects.all().delete()


    def test_anonymous_player(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

    def test_create(self):
        import ipdb; ipdb.set_trace()
        response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        data = {}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(
            response.data,
            data
        )

        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )
        create_player(None, self.user,None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.json(),
            [{'id': 1}]
        )
        create_player(None, self.user,None)
        create_player(None, self.user,None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.json(),
            [{'id': 1}],
        )



    def test_user_unique_player(self):
        [create_player(None, u ,None) for u in self.users]
        self.client.force_login(self.users[-1])
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            [{'id': 5}],
        )

    def test_user_permissions(self):
        pass
#        self.test_create()
#        import ipdb; ipdb.set_trace()
#        malicious_user = User.objects.create_user(
#        username='malicious_user', email='u@d.com', password='password')
#        create_player(None, self.user,None)
#        url  = os.path.join(self.url,str(self.user.player.pk)) +'/'
#        self.client.login(username='malicious_user', password='password')
#
#        response = self.client.get(self.url, format='json',follow=True)
##        response = self.client.get(self.url, format='json')
#        self.assertEqual(
#            response.data,
#            {"detail": "You do not have permission to perform this action."}
#        )

    #"detail": "You do not have permission to perform this action."




class GameTests(APITestCase):
    def setUp(self): 
#        import ipdb; ipdb.set_trace()
        self.url = reverse('game-list')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')
        self.users = [
            User.objects.create_user(
                username='test_user_' + str(i),
                email='u@d.com',
                password='password'
            ) for i in range(5)
        ]



    def test_anonymous_profile(self):
        import ipdb; ipdb.set_trace()
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

    def test_user_game(self):
        import ipdb; ipdb.set_trace()
        response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        data = {}
        response = self.client.post(self.url, data, format='json')
        data.update({'id': 1})
        self.assertEqual(
            response.data,
            data
        )

    def test_user_unique_game(self):
        import ipdb; ipdb.set_trace()
        self.client.force_login(self.users[0])
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        data = {}
        response = self.client.post(self.url, data, format='json')
        data.update({'id': 1})
        self.assertEqual(
            response.data,
            data
        )

        self.client.force_login(self.users[1])
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        data = {}
        response = self.client.post(self.url, data, format='json')
        data.update({'id': 1})
        self.assertEqual(
            response.data,
            data
        )

    def test_user_permissions(self):
        self.test_user_profile()
        malicious_user = User.objects.create_user(
        username='malicious_user', email='u@d.com', password='password')
        url  = os.path.join(self.url,self.user.pk) +'/'
        self.client.login(username='malicious_user', password='password')

        response = self.client.get(self.url, format='json',follow=True)
#        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail": "You do not have permission to perform this action."}
        )

    #"detail": "You do not have permission to perform this action."



