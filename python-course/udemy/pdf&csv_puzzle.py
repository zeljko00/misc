import csv
import re
import PyPDF2
def find_url():
    with open("find_the_link.csv") as file:
        csv_data=csv.reader(file)
        rows=list(csv_data)
        url=""
        for index,row in enumerate(rows):
            url+=row[index]
        return url

def find_number():
    with open("Find_the_Phone_Number.pdf","rb") as file:
        reader=PyPDF2.PdfReader(file)
        for page in reader.pages:
            match=re.search(r"\d{3}.\d{3}.\d{4}",page.extract_text())
            if match is not None:
                return match.group()
print(find_url())
print(find_number())
