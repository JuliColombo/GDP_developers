import pandas as pd


class StackOverflowReader:
    def __init__(self, csv_file):
        self.csv = csv_file

    def read(self):
        df = pd.read_csv(self.csv)
        df[['Country', 'Age1stCode', 'LanguageHaveWorkedWith']]
