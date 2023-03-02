import pandas as pd
import pycountry

from readers.models import StackOverflow


class StackOverflowReader:
    def __init__(self, csv_file):
        self.csv = csv_file

    def read(self):
        df = pd.read_csv(self.csv)

        for index, row in df[['Country', 'Age1stCode', 'LanguageHaveWorkedWith']].iterrows():
            try:
                country = pycountry.countries.get(name=row["Country"])
                if country:
                    StackOverflow.objects.create(country_name=country.name.lower(), age_first_code=row['Age1stCode'], languages_raw=row["LanguageHaveWorkedWith"])
            except Exception as e:
                print(e)