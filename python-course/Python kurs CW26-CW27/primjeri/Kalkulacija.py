from xlrd import open_workbook, cellname
from xlutils.copy import copy
import xlsxwriter


class Object(object):
    def __init__(self, bill_number, article_name, document_type, sale_price, mf_price, amount):
        """
        Klasa koja sadrzi podatke o kalkulaciji.
        :param bill_number: Broj fakture.
        :param article_name: Ime artikla.
        :param document_type: Tip kalkulacije: k ili o.
        :param sale_price: Prodajna cijena.
        :param mf_price: Cijena proizvodnje.
        :param amount: Kolicina.
        """
        self.bill_number = bill_number
        self.article_name = article_name
        self.document_type = document_type
        self.sale_price = sale_price
        self.mf_price = mf_price
        self.amount = amount


class Document(object):
    def __init__(self, bill_number, number):
        """
        :param bill_number: Broj fakture.
        :param number: Broj artikala.
        """
        self.bill_number = bill_number
        self.nr_of_objects = number



book = open_workbook("C:\\Users\\sbojanic\\Desktop\\25 DR GRUBOR.xls")

sheet = book.sheet_by_index(0)


print(sheet.nrows)
print(sheet.ncols)


for s in book.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row, col).value)
        print(','.join(str(v) for v in values))

cell = sheet.cell(2,4)
print(cell)
print(cell.value)
print(cellname(2,4))
