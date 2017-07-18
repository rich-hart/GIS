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
from accounts.views import (UserViewSet, ProfileViewSet, AddressViewSet, 
AccountViewSet)


# Serializers define the API representation.
class TribbleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tribble
        fields = (
            'owner',
        )




# ViewSets define the view behavior.
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)

router.register(r'tribbles', TribbleViewSet)

router.register(r'profile', ProfileViewSet,'profile-detail')
router.register(r'addresses', AddressViewSet)
router.register(r'users', UserViewSet)



urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social_django.urls', namespace='social')),

#    url(r'^$', home),
    url(r'^home/',home),
]
