import requests
import lxml
import bs4

result=[]
page=requests.get("http://books.toscrape.com/index.html")
soup=bs4.BeautifulSoup(page.text,"lxml")
books=soup.select(".product_pod")
for book in books:
    if len(book.select(".star-rating.Two"))>0:
        result.append(book.select("a")[1].text)

print(result)
