from django.shortcuts import render
from django.http import JsonResponse
from api.models import Event
from django.views.decorators.csrf import csrf_exempt
import dateparser
import json

# Create your views here.
def get(request):
    MAX_OBJECTS = 20

    name = request.GET.get('name')
    start_date = request.GET.get('start_date')
    organization_id = request.GET.get('organization_id')
    price = request.GET.get('price')

    events = Event.objects.all()

    if name:
        events = events.filter(name=name)
    if start_date:
        events = events.filter(start_time__date=dateparser.parse(start_date))
    if organization_id:
        events = events.filter(organization_id=organization_id)
    if price:
        events = events.filter(price=price)

    events = events[:MAX_OBJECTS]

    data = {"results": list(events.values(
        "id", "name", "price", "start_time", "end_time", "url", "organization_id"))}

    return JsonResponse(data)


@csrf_exempt
def update(request):
    try:
        received_json_data = json.loads(request.body)
    except:
        return JsonResponse({"response": "ERROR: body is not valid JSON"})

    event_id = received_json_data.get("event_id", None)
    name = received_json_data.get("name", None)
    url = received_json_data.get("url", None)
    start_time = received_json_data.get("start_time", None)
    end_time = received_json_data.get("end_time", None)
    price = received_json_data.get("price", None)
    organization_id = received_json_data.get("organization_id", None)

    try:
        event = Event.objects.get(id=event_id)
    except:
        return JsonResponse({"response": "ERROR: this event ID doesn't exist"})

    if name:
        event.name = name
    if url:
        event.url = url
    if start_time:
        start_time = dateparser.parse(
            start_time, settings={'TIMEZONE': 'UTC',  'RETURN_AS_TIMEZONE_AWARE': True})
        if start_time > event.end_time:
            return JsonResponse({"response":"ERROR: start time must be before end time"})
        event.start_time = start_time
    if end_time:
        end_time = dateparser.parse(
            end_time, settings={'TIMEZONE': 'UTC',  'RETURN_AS_TIMEZONE_AWARE': True})
        if end_time < event.start_time:
            return JsonResponse({"response": "ERROR: end time must be before start time"})
        event.end_time = end_time
    if price:
        try:
            int(price)
            event.price = price
        except:
            return JsonResponse({"response": "ERROR: price must be a number"})
    if organization_id:
        event.organization_id = organization_id
    
    event.save()

    return JsonResponse({"response": "SUCCESS"})
