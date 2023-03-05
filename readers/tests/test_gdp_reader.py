from django.test import TransactionTestCase

from readers.gdp_reader import GDPReader
from readers.models import GDP


class GDPReaderTestCase(TransactionTestCase):
    def setUp(self) -> None:
        GDPReader("readers/tests/files/test_gdp.xlsx").read(2021)

    def test_belgium_gdp_created(self):
        gdp = GDP.objects.first()
        assert gdp.country_name == "belgium"
        assert gdp.gross_domestic_product == 43330

    def test_wrong_country_gdp_not_created(self):
        assert not GDP.objects.filter(country_name="Bulgariaa").first()
