from django.db import models
from address.models import Address
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(
        User,
    )
    address = models.OneToOneField(
        Address,
    )
