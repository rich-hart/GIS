from django.core.management.base import BaseCommand, CommandError
import time
import sys
import os
from django.conf import settings
from raffle.models import Purchase, Ticket
# spawn a new thread to wait for input 
import smtplib

class Command(BaseCommand):
    
    help = 'Generate emails from purchases.'

    def add_arguments(self, parser):
        parser.add_argument('gmail_account', type=str)
        parser.add_argument('gmail_password', type=str)

    def handle(self, *args, **options):
        owner_dict = {}
        for ticket in Ticket.objects.all():
            owner_dict[ticket.owner.email] = []
        
        for ticket in Ticket.objects.all():
            owner_dict[ticket.owner.email].append(ticket.id)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(options['gmail_account'],options['gmail_password'])
        for owner_email, ticket_ids in owner_dict.items():
            msg = "YOUR GAAAYSINSPAAACE RAFFLE TICKETS!\n"\
                  "Tickets: {}".format(ticket_ids)
            from_email = options['gmail_account']
            to_email =  owner_email
            time.sleep(.25)
            server.sendmail(from_email, to_email, msg)
            print("*******************")
            print("FROM: "+ from_email)
            print("TO: " + to_email)
            print("MESSAGE: " + msg) 
        server.quit()
         
        


        
