from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'games', GameViewSet)
router.register(r'problems', ProblemViewSet)
router.register(r'solutions', SolutionViewSet)
router.register(r'challenges', ChallengeViewSet)
router.register(r'demo', DemoViewSet,basename='demo')

