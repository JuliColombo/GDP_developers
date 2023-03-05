from django.test import TestCase
from rest_framework.test import APIClient

from readers.gross_domestic_response_reader import GrossDomesticProductReader
from readers.stack_overflow_response_reader import StackOverflowResponseReader


class CountryGrossDomesticProductYoungestAgeAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        GrossDomesticProductReader("readers/tests/files/test_gdp.xlsx").read(2021)
        StackOverflowResponseReader("readers/tests/files/test_stackoverflow.csv").read()

    def test_non_european_country_returns_400_response(self):
        response = self.client.get('/processors/gdp_youngest_age/AF/')
        assert response.status_code == 400

    def test_known_european_country_returns_gdp_and_youngest_age(self):
        response = self.client.get('/processors/gdp_youngest_age/BE/').json()
        assert response['country'] == 'belgium'
        assert response['gross_domestic_product'] == 43330
        assert response['youngest_age'] == '45 - 54 years'
