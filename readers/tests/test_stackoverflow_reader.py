from django.test import TransactionTestCase

from readers.models import StackOverflow
from readers.stack_overflow_reader import StackOverflowReader


class StackOverflowReaderTestCase(TransactionTestCase):
    def setUp(self) -> None:
        StackOverflowReader("readers/tests/files/test_stackoverflow.csv").read()

    def test_bad_country_response_not_created(self):
        assert not StackOverflow.objects.filter(country_name="slovakia").first()

    def test_no_first_age_response_not_created(self):
        assert not StackOverflow.objects.filter(country_name="netherlands").first()

    def test_no_languages_programming_language_response_not_created(self):
        response = StackOverflow.objects.filter(country_name="albania").first()
        assert response
        assert not response.languages.all()

    def test_younger_5_range_0_to_4(self):
        assert StackOverflow.objects.filter(min_age_first_code=0, max_age_first_code=4).count() == 1

    def test_5_10_range_5_to_10(self):
        assert StackOverflow.objects.filter(min_age_first_code=5, max_age_first_code=10).count() == 1

    def test_11_17_range_11_to_17(self):
        assert StackOverflow.objects.filter(min_age_first_code=11, max_age_first_code=17).count() == 2

    def test_18_24_range_18_to_24(self):
        assert StackOverflow.objects.filter(min_age_first_code=18, max_age_first_code=24).count() == 1

    def test_25_34_range_25_to_34(self):
        assert StackOverflow.objects.filter(min_age_first_code=25, max_age_first_code=34).count() == 1

    def test_35_44_range_35_to_44(self):
        assert StackOverflow.objects.filter(min_age_first_code=35, max_age_first_code=44).count() == 1

    def test_45_54_range_45_to_54(self):
        assert StackOverflow.objects.filter(min_age_first_code=45, max_age_first_code=54).count() == 1

    def test_55_64_range_55_to_64(self):
        assert StackOverflow.objects.filter(min_age_first_code=55, max_age_first_code=64).count() == 1

    def test_older_64_range_65_to_none(self):
        assert StackOverflow.objects.filter(min_age_first_code=65, max_age_first_code=None).count() == 1
