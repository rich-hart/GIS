import unittest
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

def join_paths(*args):
    return os.path.join(*args)+'/'

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
            [{'id': 1,'game_set': []}]
        )
        create_player(None, self.user,None)
        create_player(None, self.user,None)
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.json(),
            [{'id': 1,'game_set': []}],
        )



    def test_user_unique_player(self):
        [create_player(None, u ,None) for u in self.users]
        self.client.force_login(self.users[-1])
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.json(),
            [{'id': 5,'game_set': []}],
        )

    def test_join_featured_game(self):
        #[create_player(None, u ,None) for u in self.users]
        create_player(None,self.user, None)
        game = Game()
        game.save()
        tag = Tag(category=Tag.Type.featured.value,game=game)
        tag.save()
        self.client.force_login(self.user)
        play_featured_game_url = join_paths(
            self.url,
            ##str(self.user.player.pk),
            'join_featured_game'
        )
        response = self.client.put(play_featured_game_url, format='json')
        expected = {'id': 1, 'game_set': [{'id': 1, 'tags': [{'category': 'FE', 'id': 1, 'other_category': None}]}]}
        returned = response.json()
        self.assertEqual(
            expected, returned
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
        self.player = Player.objects.create(user=self.user)

        self.users = [
            User.objects.create_user(
                username='test_user_' + str(i),
                email='u@d.com',
                password='password'
            ) for i in range(5)
        ]
        self.players = [
            Player.objects.create(user=user)
            for user in self.users
        ]

    def tearDown(self):
        Game.objects.all().delete()

    def test_anonymous_profile(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

#    def test_new_game(self):
#        self.client.force_login(self.user)
#        response = self.client.get(self.url, format='json')
#        self.assertEqual(
#            response.json(),
#            [],
#        )
#
#        response = self.client.post(self.url+'new_game/', format='json')
#        self.assertDictEqual(
#            response.json(),
#            {'detail': 'You do not have permission to perform this action.'},
#        )
#        self.user.is_staff = True
#        self.user.save()
#
#        response = self.client.post(self.url+'new_game/', format='json')
#
#        self.assertEqual(
#            response.json(),
#            {'id': 1,'tags': []},
#        )
#        expected = [p for p in Player.objects.all()]
#        returned = [p for p in Game.objects.get(pk=1).players.all()]
#        self.assertListEqual(expected, returned)
#
#    def test_new_featured_game(self):
#        self.test_new_game()
#        response = self.client.put(self.url+'1/feature/', format='json')
#        game = Game.objects.get(pk=1)
#        self.assertEqual(
#            response.json(),
#            {'id': 1, 'tags': [{'id': 1, 'category': 'FE', 'other_category': None}]},
#        )
#
#    def test_next_challenge(self):
#        self.test_new_game()
#        self.answer = Answer.objects.create(text='Answer.')
#        self.question = Question.objects.create(text='Question?')
#        self.challenge = Challenge.objects.create(game_id=1, problem=self.question, solution=self.answer)
#        response = self.client.get(self.url+'1/next_challenge/', format='json')
#
#
#
#        self.assertEqual(
#            response.json(),
#            {'id': 1, 'problem': {'id': 1, 'question': {'id': 1, 'text': 'Question?'}}}
#        )


class ChallengeTests(APITestCase):
    def setUp(self): 
#        import ipdb; ipdb.set_trace()
        self.url = reverse('challenge-list')
        self.user = User.objects.create_user(
            username='test_user', email='u@d.com', password='password')
        self.game = Game.objects.create()

        self.player = Player.objects.create(user=self.user)
        self.player.game_set.add(self.game)
        self.player.save()

        self.users = [
            User.objects.create_user(
                username='test_user_' + str(i),
                email='u@d.com',
                password='password'
            ) for i in range(5)
        ]
        self.players = [
        ]
        for user in self.users:
            player = Player.objects.create(user=user)
            player.game_set.add(self.game)
            self.players.append(player)

        self.answer = Answer.objects.create(text='Answer.')
        self.question = Question.objects.create(text='Question?')
        self.challenge = Challenge.objects.create(game=self.game, problem=self.question, solution=self.answer)
        self.challenges =[]
        for _ in range(5):
            answer = Answer.objects.create(text='Answer.')
            question = Question.objects.create(text='Question?')
            challenge = Challenge.objects.create(game=self.game, problem=question, solution=answer)
            self.challenges.append(challenge)
    def tearDown(self):
        Achievement.objects.all().delete()
        Game.objects.all().delete()

    def test_anonymous_profile(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(
            response.data,
            {"detail":"Authentication credentials were not provided."}
        )

#    def test_solve(self):
#        self.client.force_login(self.user)
#        response = self.client.get(self.url, format='json')
#        self.assertEqual(
#            len(response.json()),
#            6,
#        )
#        returned = Achievement.objects.filter(player=self.user.player,challenge=self.challenge).exists()
#        self.assertFalse(returned) 
#        self.client.put(self.url+'1/solve/', data={'answer':'answer'},format='json')
#        returned = Achievement.objects.filter(player=self.user.player,challenge=self.challenge).exists()
#        self.assertTrue(returned) 
#
