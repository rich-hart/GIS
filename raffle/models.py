from __future__ import unicode_literals

from django.db import models


class Purchaser(models.Model):
    email = models.EmailField()
    first_name = models.CharField(
        max_length = 255,
    )
    last_name = models.CharField(
        max_length = 255,
    )


class Ticket(models.Model):
    owner = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
    drawed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id)

class Draw(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

class Purchase(models.Model):
    SINGLE = '1X'
    FIVE_BUNDLE = '5X'
    TEN_BUNDLE = '10X'
    TICKET_CHOICES = (
        (SINGLE, '1 Ticket for $10'),
        (FIVE_BUNDLE, '5 Tickets for $40'),
        (TEN_BUNDLE, '10 Tickets for $70'),
    )
    item = models.CharField(
        max_length=3,
        choices=TICKET_CHOICES,
        default=SINGLE,
    )
    buyer = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Prize(models.Model):
    image = models.URLField()
    title = models.CharField(max_length = 255)
    description = models.TextField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True)

