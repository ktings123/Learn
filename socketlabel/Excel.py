import xlrd


class readExcel(object):
    def __init__(self, path):
        self.path = path

    def getSheet(self):
        exc = xlrd.open_workbook(self.path)
        sheet = exc.sheet_by_index(0)
        return sheet

    def getRow(self):
        row = self.getSheet().nrows
        return row

    def getCol(self):
        col = self.getSheet().ncols
        return col


