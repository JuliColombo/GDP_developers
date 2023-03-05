from django.test import TransactionTestCase

from readers.gross_domestic_response_reader import GrossDomesticProductReader
from readers.models import GrossDomesticProduct


class GrossDomesticProductReaderTestCase(TransactionTestCase):
    def setUp(self) -> None:
        GrossDomesticProductReader("readers/tests/files/test_gdp.xlsx").read(2021)

    def test_belgium_gdp_created(self):
        gdp = GrossDomesticProduct.objects.first()
        assert gdp.country_name == "belgium"
        assert gdp.gross_domestic_product == 43330

    def test_wrong_country_gdp_not_created(self):
        assert not GrossDomesticProduct.objects.filter(country_name="Bulgariaa").first()
