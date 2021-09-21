
import json
from unittest import TestCase
from attr import s
from django.test import Client
from django.urls import reverse
import pytest

@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client=Client()
        self.url=reverse('companies-list')
        return super().setUp()
    def tearDown(self) -> None:
        return super().tearDown()



class TestGetCompanies(BasicCompanyAPITestCase):
    def test_zero_companies_sholud_return_empty_list(self)->None:
        response=self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(json.loads(response.content),[])

class TestPost(BasicCompanyAPITestCase):
    def test_create_company_without_args_should_fail(self)->None:
        response=self.client.post(self.url)
        self.assertEqual(response.status_code,400)
