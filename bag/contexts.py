from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from events.models import Event

def bag_contents(request):

    bag_items = []
    total = 0
    event_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            event = get_object_or_404(Event, pk=item_id)
            total += item_data * event.price
            event_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'event': event,
            })
        else:
            event = get_object_or_404(Event, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * event.price
                event_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'event': event,
                    'size': size,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'event_count': event_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
