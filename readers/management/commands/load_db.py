from django.core.management.base import BaseCommand, CommandError

from readers.gdp_reader import GDPReader
from readers.models import StackOverflow, GDP
from readers.stack_overflow_reader import StackOverflowReader


class Command(BaseCommand):
    help = 'Load db with stackoverflow and gdp'

    def handle(self, *args, **options):
        GDP.objects.all().delete()
        GDPReader("readers/files/tec00001_page_spreadsheet.xlsx").read(2021)

        StackOverflow.objects.all().delete()
        StackOverflowReader("readers/files/survey_results_public.csv").read(2021)