"""gis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import home

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from tribbles.models import Tribble
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from tribbles.views import TribbleViewSet
# Serializers define the API representation.
class TribbleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tribble
        fields = (
            'owner',
        )



# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'tribbles', TribbleViewSet)

router.register(r'users', UserViewSet)



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social_django.urls', namespace='social')),

#    url(r'^$', home),
    url(r'^home/',home),
]
