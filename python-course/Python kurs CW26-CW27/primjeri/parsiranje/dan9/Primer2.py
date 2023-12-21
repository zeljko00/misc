from xlrd import open_workbook, cellname

book = open_workbook('zadatak_excel.xls')
sheet = book.sheet_by_index(0)

print sheet.name
print sheet.nrows
print sheet.ncols

TerryJonesMovies = ""

for row_index in range(sheet.nrows):
    if "Terry Jones" in sheet.cell(row_index,2).value:
        #print sheet.cell(row_index,2).value
        print ("%s : %s")%((sheet.cell(row_index,0).value),(str)(sheet.cell(row_index,1).value))
        TerryJonesMovies = TerryJonesMovies + ''.join((str)(sheet.cell(row_index,0).value))+':'
        TerryJonesMovies = TerryJonesMovies + ''.join((str)(sheet.cell(row_index,1).value))+'\n'
        with(open('xls_output.txt','w')) as txt_file:
            txt_file.write(TerryJonesMovies)


