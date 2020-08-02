from django.shortcuts import render
from .models import Event

# Create your views here.

def all_events(request):
    """ A view to show all products, including sorting and search queries """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/events.html', context)