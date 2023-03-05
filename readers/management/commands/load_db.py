from django.core.management.base import BaseCommand, CommandError

from readers.gross_domestic_response_reader import GrossDomesticProductReader
from readers.models import GrossDomesticProduct, StackOverflowResponse
from readers.stack_overflow_response_reader import StackOverflowResponseReader


class Command(BaseCommand):
    help = 'Load db with stackoverflow and gdp'

    def handle(self, *args, **options):
        GrossDomesticProduct.objects.all().delete()
        GrossDomesticProductReader("readers/files/tec00001_page_spreadsheet.xlsx").read(2021)

        StackOverflowResponse.objects.all().delete()
        StackOverflowResponseReader("readers/files/survey_results_public.csv").read()