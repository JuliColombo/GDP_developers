import pandas as pd
import pycountry

from readers.models import GDP


class GDPReader:
    def __init__(self, xlsx_file):
        self.xslx = xlsx_file

    def read(self):
        df = pd.read_excel(self.xslx, sheet_name="Sheet 1", skiprows=8)

        for index, row in df[['TIME', '2021']].iterrows():
            try:
                country = pycountry.countries.get(name=row["TIME"])
                if country:
                    GDP.objects.create(country_name=country.name.lower(), country_iso=country.alpha_2, gross_domestic_product=int(row['2021']))
            except Exception as e:
                print(e)
