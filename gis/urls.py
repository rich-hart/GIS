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
from .views import (
    home, 
    demo, 
    facebook, 
    profile_form,
    qr_code_validator,
    raffle,
)

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from tribbles.models import Tribble
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from tribbles.views import TribbleViewSet
from accounts.views import (
    UserViewSet, 
    ProfileViewSet, 
    AddressViewSet, 
    AccountViewSet, 
    GoogleIDViewSet
)
from raffle.views import (
   PurchaseViewSet, 
   TicketViewSet,
   PurchaserViewSet,
)
from django.conf import settings
from django.conf.urls.static import static

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
router.register(r'accounts', AccountViewSet, base_name='account')

router.register(r'tribbles', TribbleViewSet)

router.register(r'profile', ProfileViewSet, base_name='profile')
router.register(r'addresses', AddressViewSet)
router.register(r'users', UserViewSet)
router.register(r'google_ids', GoogleIDViewSet)
router.register(r'purchase', PurchaseViewSet)
router.register(r'purchaser', PurchaserViewSet)

router.register(r'ticket', TicketViewSet)


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),

    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social_django.urls', namespace='social')),

    url(r'^$', home, name='home'),
#    url(r'^home/',home,name='home'),
    url(r'^profile_form/',profile_form),
    url(r'^qr_code_validator/(?P<key>.+)/$',qr_code_validator),
    url(r'^raffle/',raffle),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + [url(r'^demo/',demo)]

if settings.DEBUG:
    urlpatterns = urlpatterns + [url(r'^facebook/',facebook)]
