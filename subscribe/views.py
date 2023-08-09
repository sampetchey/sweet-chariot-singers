from django.shortcuts import render
from django.contrib import messages

from .forms import Membershipform
from .server import checkout_session

def subscribe(request):
    fee = request.session.get('fee', {})
    membership_form = Membershipform
    template = 'subscribe/subscribe.html'
    context = {
        'membership_form': membership_form,
    }

    return render(request, template, context)





