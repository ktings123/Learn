import xlrd


def getSheet():
    fileData = []
    table = xlrd.open_workbook(r'C:\Users\82008947\Desktop\Itop\testfile.xlsx')
    sheet = table.sheet_by_name('Sheet1')
    nrows = sheet.nrows
    ncols = sheet.ncols
    for attr in range(ncols):
        for val in range(nrows):
            fileData.append(sheet.cell(val, attr).value)
    return fileData

ss = getSheet()
tt = dict(ss)
print(tt)
method = getSheet()[1]
url = getSheet()[3]
data = getSheet()[5]

