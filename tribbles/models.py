from django.db import models
from django.contrib.auth.models import User
class Tribble(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    key = models.CharField(max_length=32) 

