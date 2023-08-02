from django.contrib import admin
from .models import Membership

class MembershipAdmin(admin.ModelAdmin):
    readonly_fields = ('membership_fee', 'date',)
    fields = ('date', 'full_name', 'email', 'phone_number', 
              'postcode', 'town_or_city', 'street_address1', 
              'street_address2', 'voice_type', 'membership_fee',)

admin.site.register(Membership, MembershipAdmin)