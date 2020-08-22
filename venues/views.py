from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Venues

# Create your views here.


def venues(request):
    """ A view to show all venues, including sorting and search queries """

    venues = Venues.objects.all()
    query = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                venues = venues.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            venues = venues.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('venues'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            venues = venues.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'venues': venues,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'venues/venues.html', context)