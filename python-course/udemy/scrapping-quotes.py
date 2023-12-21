import requests
import lxml
import bs4

def scrape_page():
    result=[]
    tags=[]
    page=requests.get("http://quotes.toscrape.com/")
    soup=bs4.BeautifulSoup(page.text,"lxml")

    quotes=soup.select(".quote")
    top_ten=soup.select(".tag-item > a")
    for quote in quotes:
        result.append((quote.select(".text")[0].text,quote.select(".author")[0].text))
    for tag in top_ten:
        tags.append(tag.text)
    return(result,tags)
def scrape_pages():
    scrape=True
    counter=1
    auths=set()
    while scrape:
        page = requests.get("http://quotes.toscrape.com/page/"+str(counter))
        if page.status_code==200:
            soup = bs4.BeautifulSoup(page.text, "lxml")
            quotes = soup.select(".quote")
            if len(quotes)==0:
                break;
            for quote in quotes:
                auths.add(quote.select(".author")[0].text)
            counter+=1
        else:
            scrape=False
    return auths


# print(scrape_page())
print(scrape_pages())