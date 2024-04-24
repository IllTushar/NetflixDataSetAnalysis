import pandas as pd


class DataSet:
    @staticmethod
    def dataFileSet():
        data = {"a": [1, 2, 3, 4], "b": [1, 2, 3, 4], "c": [1, 2, 3, 4]}
        d = pd.DataFrame(data)
        d.to_csv("Fist_Csv.csv", index=False, header=['x', 'y', 'z'])
