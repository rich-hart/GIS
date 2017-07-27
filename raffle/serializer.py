from rest_framework import serializers
from .models import Purchaser, Purchase, Ticket 


class PurchaserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchaser
        fields = ('email','first_name','last_name')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
#    purchasers = Purchaser.objects.all()
#    purchaser = PurchaserSerializer(many=False)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Purchase
        fields = (
            'id',
            'item',
            'email',
            'first_name',
            'last_name',
            'buyer',
#            'purchaser',
        )
        read_only_fields = ('buyer',)
        write_only_fields = ('first_name','last_name','buyer')
        depth = 1        
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'owner')
        read_only_fields = ('owner',)


 
