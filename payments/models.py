from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.conf import settings

class Membership(models.Model):
    LEAD = "Lead"
    TENOR = "Tenor"
    BARITONE = "Baritone"
    BASS = "Bass"
    ANY = "Any"
    UNKNOWN = "Unknown"
    VOICE_TYPE_CHOICES = [
        (LEAD, "Lead - Singing the tune"),
        (TENOR, "Tenor - Normally a descant higher than the tune"),
        (BARITONE, "Baritone - Similar range to Lead, but in harmony with it"),
        (BASS, "Bass - Low register, normally singing the root of the harmony"),
        (ANY, "Versatile - Comfortable singing any part"),
        (UNKNOWN, "I'm not sure"),
    ]

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    voice_type = models.CharField(
        max_length=80,
        choices=VOICE_TYPE_CHOICES, 
        default=LEAD,
        )
    date = models.DateTimeField(auto_now_add=True)
    membership_fee = models.IntegerField(null=False, default=30)

    def __str__(self):
        return self.full_name
