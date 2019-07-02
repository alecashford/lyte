from django.db import models


class Event(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=1000)
    url = models.CharField(max_length=2000)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=1.0)
    organization_id = models.IntegerField(default=1)
