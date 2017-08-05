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
#        import ipdb; ipdb.set_trace()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(options['gmail_account'],options['gmail_password'])
        from_email = options['gmail_account']
        for purchase in Purchase.objects.all():
            to_email = purchase.buyer.email
            if purchase.item == "1X":
                units = "1 Ticket for $10"
            elif purchase.item == "5X": 
                units = "5 Tickets for $40"
            elif purchase.item == "10X":
                units = "10 Tickets for $70"           
            msg = "\n GAAAYSINSPAAACE Purchase: {0}.\n THANK YOU!!!! \n".format(units)                 
            time.sleep(.25) 
            server.sendmail(from_email, to_email, msg) 
            print("*******************")
            print("FROM: "+ from_email)
            print("TO: " + to_email)
            print("MESSAGE: " + msg) 

        server.quit()
         
        


        
