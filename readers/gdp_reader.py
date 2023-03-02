import pandas as pd


class GDPReader:
    def __init__(self, xlsx_file):
        self.xslx = xlsx_file

    def read(self):
        df = pd.read_excel(self.xslx, sheet_name="Sheet 1", skiprows=8)
        df[['TIME', '2021']]
