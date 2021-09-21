
import json
from unittest import TestCase
from django.test import Client
from django.urls import reverse
import pytest






@pytest.mark.django_db
class TestGetCompanies(TestCase):


    def setUp(self) -> None:
        self.client=Client()
        self.url=reverse('companies-list')
        return super().setUp()

    def test_zero_companies_sholud_return_empty_list(self)->None:
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content),[])

