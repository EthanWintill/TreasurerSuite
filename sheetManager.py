import pandas as pd
import numpy as np
import gspread

def getOutstanding():
    gc = gspread.service_account('/Users/mymac/Downloads/Career-Stuff/Projects/TreasurerSuite/SheetKey/key.json')
    sh = gc.open("S23Dues")
    rows = sh.sheet1.get_all_values()

    dues = pd.DataFrame(rows)
    outstanding = dues.iloc[3:,18:21]
    outstanding.columns = ['FirstName','LastName','Outstanding']
    outstanding.replace('', np.nan, inplace=True)
    outstanding.dropna(inplace=True)

    return outstanding.values
