from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User, Group


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
#from myproject.apps.core.models import Account
from selenium import webdriver
from django.test import LiveServerTestCase
import shutil
import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import urllib


from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory


class ProfileTests(APITestCase):
    def setUp(self): 
#        import ipdb; ipdb.set_trace()
        self.url = reverse('profile-list')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')

    def test_anonymous_profile(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

    def test_user_profile(self):

        response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            []
        )

        #response = self.client.get(self.url, format='json')
        self.client.login(username='test_user', password='password')
        data = {'address' : 'number street, city state zip'}
        response = self.client.post(self.url, data, format='json')
        #data.update({'owner': 1})
        self.assertEqual(
            response.data,
            data
        )
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data[0],
            data
        )
        def test_user_permissions(self):
            self.test_user_profile()
            malicious_user = User.objects.create_user(
            username='malicious_user', email='u@d.com', password='password')
            url  = os.path.join(self.url,self.user.pk) +'/'
            self.client.login(username='malicious_user', password='password')

            response = self.client.get(self.url, format='json',follow=True)
#            response = self.client.get(self.url, format='json')
            self.assertEqual(
                response.data,
                {"detail": "You do not have permission to perform this action."}
            )

        #"detail": "You do not have permission to perform this action."



