from rest_framework import serializers
from .models import Purchaser, Purchase, Ticket, Prize

class PurchaserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchaser
        fields = ('email','first_name','last_name')

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
#    purchasers = Purchaser.objects.all()
    buyer = PurchaserSerializer()
#    email = serializers.ReadOnlyField(source='buyer.email')
#    first_name = serializers.ReadOnlyField(source='buyer.first_name')
#    last_name = serializers.ReadOnlyField(source='buyer.last_name')

    class Meta:
        model = Purchase
        fields = (
            'id',
            'item',
#            'email',
#            'first_name',
#            'last_name',
            'buyer',
            'time_stamp',
#            'purchaser',
        )
        read_only_fields = ('buyer','time_stamp')
#        write_only_fields = ('first_name','last_name','buyer','email','item')
#        depth = 1      
    def create(self, validated_data):
#        import ipdb; ipdb.set_trace()
        buyer_data = validated_data.pop('buyer')
        purchaser = Purchaser(**buyer_data)
        purchaser.save()
        purchase = Purchase(item=validated_data['item'],buyer=purchaser)
        purchase.save()
#        if validated_data['item']=='1X':
#            units = 1
#        elif validated_data['item']=='5X':
#            units = 5
#        elif validated_data['item']=='10X':
#            units = 10
#        else:
#            #RAISE ERROR
#            units = 0
#        for i in range(0, units):
#            ticket = Ticket(owner = purchaser)
#            ticket.save()
        return purchase
#        tracks_data = validated_data.pop('tracks')
#        album = Album.objects.create(**validated_data)
#        for track_data in tracks_data:
#            Track.objects.create(album=album, **track_data)
#        return album
 
class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'owner','drawed')
        read_only_fields = ('owner','drawed')

class PrizeSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='prize-highlight', format='html')
    class Meta:
        model = Prize
        fields = ('id', 'title','image','description','ticket','highlight')
        read_only_fields = ('ticket',)

 
