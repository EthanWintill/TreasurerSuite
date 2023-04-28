import pandas as pd
import numpy as np
import gspread
from datetime import datetime

gc = gspread.service_account('/Users/mymac/Desktop/Career-Stuff/Projects/TreasurerSuite/TreasurerSuite/SheetKey/key.json')
sh = gc.open("S23Dues")
rows = sh.sheet1.get_all_values()
dues = pd.DataFrame(rows)
dues.columns = ['','First','Last','','fines','dues','payment1','payment2','payment3','payment4','','','','','','','','','','','']

numBrothers = dues.iloc[1][12]

def getOutstanding():
    outstanding = dues.iloc[3:,18:21]
    outstanding.replace('', np.nan, inplace=True)
    outstanding.dropna(inplace=True)
    return outstanding.values



def fine(first: str, last: str, amount: int):
    brother = dues[(dues['First']==first) &  (dues['Last']==last)]
    if(brother.empty):
        print('ERROR: NAME NOT FOUND!!')
        exit()
    brotherRow = dues.index[(dues['First']==first) &  (dues['Last']==last)].tolist()[0] + 1
    currentFine = brother.values[0][4][1:]
    if(currentFine != ''):
        amount += float(currentFine)
    sh.sheet1.update_cell(row=brotherRow, col=5,value = amount)


def printList():
    list = getOutstanding()
    for entry in list:
        print(f'{entry[0]} {entry[1]} {entry[2]}')


printList()