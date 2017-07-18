from rest_framework import routers, serializers, viewsets
from .models import Tribble
class TribbleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tribble
        fields = (
            'owner',
        )
