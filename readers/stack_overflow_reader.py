import pandas as pd
import pycountry

from readers.models import StackOverflow, ProgrammingLanguageResponse


class StackOverflowReader:
    def __init__(self, csv_file):
        self.csv = csv_file

    def age_range(self, range_str):
        match range_str:
            case 'Younger than 5 years':
                return {'min': 0, 'max': 4}
            case '5 - 10 years':
                return {'min': 5, 'max': 10}
            case '11 - 17 years':
                return {'min': 11, 'max': 17}
            case '18 - 24 years':
                return {'min': 18, 'max': 24}
            case '25 - 34 years':
                return {'min': 25, 'max': 34}
            case '35 - 44 years':
                return {'min': 35, 'max': 44}
            case '45 - 54 years':
                return {'min': 45, 'max': 54}
            case '55 - 64 years':
                return {'min': 55, 'max': 64}
            case 'Older than 64 years':
                return {'min': 65, 'max': None}

    def read(self):
        df = pd.read_csv(self.csv)

        for index, row in df[['Country', 'Age1stCode', 'LanguageHaveWorkedWith']].iterrows():
            try:
                country = pycountry.countries.get(name=row["Country"])
                age_range = self.age_range(row['Age1stCode'])
                if country and age_range:
                    survey_response = StackOverflow.objects.create(country_name=country.name.lower(),
                                                                   min_age_first_code=age_range['min'],
                                                                   max_age_first_code=age_range['max'])
                    if type(row["LanguageHaveWorkedWith"]) is str:
                        for language in row["LanguageHaveWorkedWith"].split(";"):
                            ProgrammingLanguageResponse.objects.create(name=language, survey_response=survey_response)
                    print("New survey response created")
            except Exception as e:
                print(e)