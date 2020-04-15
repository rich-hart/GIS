from django.db import models
#from address.models import Address as DjangoAddress
from django.contrib.auth.models import User


#class Address(DjangoAddress):
#    google_id = models.CharField(max_length=255)


class Profile(models.Model):
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
#    address = models.OneToOneField(
#        Address,
#        null = True
#    )


