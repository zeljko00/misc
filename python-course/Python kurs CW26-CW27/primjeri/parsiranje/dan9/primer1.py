from xlrd import open_workbook
book = open_workbook('primer_1.xls')

from xlrd import open_workbook
wb = open_workbook('primer_1.xls')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print ','.join(values)
