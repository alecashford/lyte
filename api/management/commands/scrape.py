import os
import requests
import dateparser
import random
import decimal
from django.core.management.base import BaseCommand, CommandError
from api.models import Event

class Command(BaseCommand):
    help = 'Populates db with scraped eventbrite data'

    token = os.environ.get("EVENTBRITE_TOKEN")
    base_query = "https://www.eventbriteapi.com/v3/events/search/?token={}".format(
        token)
    

    def handle(self, *args, **options):
        for i in range(1, 21):
            paginated_query = "{}&page={}".format(self.base_query, i)
            r = requests.get(paginated_query)
            events = r.json()["events"]

            for event in events:
                Event.objects.update_or_create(
                    id=event["id"],
                    name=event["name"]["text"],
                    url=event["url"],
                    start_time=dateparser.parse(event["start"]["utc"],
                                    settings={'TIMEZONE': 'UTC', 'RETURN_AS_TIMEZONE_AWARE': True}),
                    end_time=dateparser.parse(event["end"]["utc"],
                                    settings={'TIMEZONE': 'UTC', 'RETURN_AS_TIMEZONE_AWARE': True}),
                    organization_id=event["organization_id"],
                    price=decimal.Decimal(
                        random.randrange(1000, 5000))/100
                ),
