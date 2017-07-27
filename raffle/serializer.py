from rest_framework import serializers
from .models import Purchaser, Purchase, Ticket 


class PurchaserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchaser
        fields = ('id','email','first_name','last_name')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    purchaser = PurchaserSerializer()
    class Meta:
        model = Purchase
        fields = ('id','item','purchaser')

#    def create(self, validated_data):
#        import ipdb; ipdb.set_trace()
#        pass
        
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'owner')
        read_only_fields = ('owner',)


 
