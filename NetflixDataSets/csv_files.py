import pandas as pd


class CSV_Data:
    @staticmethod
    def csv_data_file():
        csv_file = pd.read_csv(r"C:\Users\gtush\Desktop\DataSets\netflix_titles.csv", low_memory=False)
        return csv_file
