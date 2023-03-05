from django.test import TestCase
from rest_framework.test import APIClient

from readers.gdp_reader import GDPReader
from readers.stack_overflow_reader import StackOverflowReader


class CountryGDPYoungestAgeAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        GDPReader("readers/tests/files/test_gdp.xlsx").read(2021)
        StackOverflowReader("readers/tests/files/test_stackoverflow.csv").read()

    def test_non_european_country_returns_400_response(self):
        response = self.client.post('/processors/gdp_youngest_age', data={'iso_code': 'AF'}, format='json')
        assert response.status_code == 400

    def test_known_european_country_returns_gdp_and_youngest_age(self):
        response = self.client.post('/processors/gdp_youngest_age', data={'iso_code': 'BE'}, format='json').json()
        assert response['country'] == 'belgium'
        assert response['gross_domestic_product'] == 43330
        assert response['youngest_age'] == '45 - 54 years'
