from django.db import models

from simple_history.models import HistoricalRecords

class TestModel(models.Model):
    field = models.IntegerField(default=1)

    history = HistoricalRecords()
