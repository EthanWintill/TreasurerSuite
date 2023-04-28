import sheetManager as sheet
import groupmeManager as messanger

def translateTest():
    for brother in  sheet.getOutstanding()[:-1]:
        name = brother[0] + ' ' + brother[1]
        brotherGroupmeObject = messanger.getBrother(name)
        print(brotherGroupmeObject)
