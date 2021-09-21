
import json
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import pytest






@pytest.mark.django_db
class TestGetCompanies(TestCase):
    def test_zero_companies_sholud_return_empty_list(self)->None:
        client=Client()
        url=reverse('companies-list')
        response=client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content),[])

