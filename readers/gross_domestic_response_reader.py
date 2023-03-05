import pandas as pd
import pycountry

from readers.models import GrossDomesticProduct


class GrossDomesticProductReader:
    def __init__(self, xlsx_file):
        self.xslx = xlsx_file

    def read(self, year):
        df = pd.read_excel(self.xslx, sheet_name="Sheet 1", skiprows=8)

        for index, row in df[['TIME', str(year)]].iterrows():
            try:
                country = pycountry.countries.get(name=row["TIME"])
                if country:
                    GrossDomesticProduct.objects.create(country_name=country.name.lower(), country_iso=country.alpha_2, gross_domestic_product=int(row[str(year)]))
            except Exception as e:
                print(e)
