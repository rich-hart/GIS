from django.core.management.base import BaseCommand, CommandError
from raffle.models import Purchase, Ticket, Prize
import random
import threading
user_input = False
import time
import sys
import os
# spawn a new thread to wait for input 


class Command(BaseCommand):
    
    help = 'Generate ticket from purchases.'

    def add_arguments(self, parser):
        parser.add_argument('prize_id', type=int)

    def handle(self, *args, **options):

        global user_input
        prize = Prize.objects.get(id= options['prize_id'])
        if not prize.ticket:
#           import ipdb; ipdb.set_trace();
           tickets = [t for t in Ticket.objects.filter(drawed=False)]
           random.shuffle(tickets)
           input("Start Raffle! ")
           pause_time = .0001;
           start_time = time.time()
           while(time.time()-start_time< 25):
               pause_time = pause_time * 1.01
               time.sleep(pause_time)
               ticket = tickets.pop(0)
#               print(ticket)
               os.system('clear')
               print('  {0} {1} {2}'.format( ticket, ticket.owner.first_name,ticket.owner.last_name))
               tickets.append(ticket)
           ticket.drawed=True
           ticket.save()
           prize.ticket = ticket
           prize.save()
        os.system('clear')
        print(prize.ticket)
#           while(not user_input):
#               for t in tickets:
#                   print(t)
        print("WINNER!!!!!")
        print("Congratulations {0} {1}!!!!!".format(prize.ticket.owner.first_name,prize.ticket.owner.last_name))


