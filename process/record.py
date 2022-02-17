#file includes a class that deals with generating the excel output

import pandas as pd


class dataRecorder:
    def __init__(self,_filename): #set the name of the file
        self.excelFilename = _filename
        self.writer = pd.ExcelWriter(self.excelFilename, engine='xlsxwriter')

    def initialiseNewSheet(self,_sheetTag,_titleTag): #set new sheet in the workbook
        self.sheetTag = _sheetTag
        self.title = _titleTag

    def setTitle(self): #set title for each sheet
        workbook  = self.writer.book
        worksheet = self.writer.sheets[self.sheetTag]
        header_format = workbook.add_format({
        'bold': True,
        'text_wrap': False,
        'valign': 'top',
        'border': 1})
        worksheet.write_string(0, 0, self.title,header_format)
                
    def writeToExcel(self,_dataDict,_columnList): #write data to excel file
        df = pd.DataFrame(list(_dataDict.items()),columns = _columnList)
        df.to_excel(self.writer, sheet_name=self.sheetTag,startrow=2)
        self.setTitle()


    def saveFile(self): #save file
        self.writer.save()


