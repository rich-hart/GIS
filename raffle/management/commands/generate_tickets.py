from django.core.management.base import BaseCommand, CommandError
from raffle.models import Purchase, Ticket


class Command(BaseCommand):
    help = 'Generate ticket from purchases.'

    def handle(self, *args, **options):
        for purchase in Purchase.objects.all():
            units = 0
            if purchase.item=='1X':
                units = 1
            elif purchase.item=='5X':
                units = 5
            elif purchase.item=='10X':
                units = 10
            else:
                units = 0
            for i in range(0, units):
                ticket = Ticket(owner = purchase.buyer)
                ticket.save()
           
