from django.test import TestCase
from . import models

class Test(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj = models.TestModel.objects.create()
        cls.obj.field = 100
        cls.obj.save()

    def test_historical_manager_works_with_drf(self):
        response = self.client.get('/testurl/')
        self.assertEqual(response.status_code, 200)

    def test_most_recent_works_with_excluded_fields(self):
        latest = self.obj.history.most_recent()
        self.assertEqual(latest.field == 100)
