from django.conf.urls import url, include

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(
    r'avatar',
    NewAvatarViewSet,
    basename='avatar'
)


router.register(
    r'players',
    NewPlayerViewSet,
    basename='player'
)

router.register(
    r'games',
    NewGameViewSet
)

router.register(
    r'completed_challenges',
    NewCompletedChallengeViewSet,
    basename='completed_challenge',
)

router.register(
    r'challenges',
    NewChallengeViewSet,
    basename='challenge'
)

router.register(
    r'awards',
    AwardViewSet,
    basename='award'
)

router.register(
    r'rewards',
    NewRewardViewSet
)

#router.register(r'avatar', AvatarViewSet, basename='avatar')
#router.register(r'players', PlayerViewSet, basename='player')
#router.register(r'games', GameViewSet)
#router.register(r'problems', ProblemViewSet)
#router.register(r'solutions', SolutionViewSet)
#router.register(r'challenges', ChallengeViewSet)
#router.register(r'demo', DemoViewSet,basename='demo')
#router.register(r'hidden_challenges', HiddenChallengeViewSet,basename='hidden_challenge')
#router.register(r'rewards', RewardViewSet)

