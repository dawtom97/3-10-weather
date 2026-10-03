import pandas as pd
import os
from config import App

def create_file(data):
    FILE = App.EXCEL_FILEPATH
    try:
        new_df = pd.DataFrame(data)
        if os.path.exists(FILE):
            old_df = pd.read_excel(FILE)
            concat_df = pd.concat([old_df, new_df])
            concat_df.to_excel(FILE,index=False)
        else:
            new_df.to_excel(FILE, index=False)
    except Exception as err:
        print(err)


def read_file():
    FILE = App.EXCEL_FILEPATH
    try:
        df = pd.read_excel(FILE)
        return df
    except Exception as err:
        print(err)
