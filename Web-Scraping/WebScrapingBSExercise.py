import requests
import bs4
import WebScrapingBSLesson as WSBSL

html = WSBSL.getHTML('http://books.toscrape.com/')
soup = bs4.BeautifulSoup(html,'html.parser')

def str_to_int(strnum):
    strnums = ['one','two','three','four','five']
    realnums = [1,2,3,4,5]
    strnum = strnum.lower()
    index = strnums.index(strnum)
    realnum = realnums[index]
    return realnum

articles = soup.find_all('article')
print(type(articles))

books = []

for pod in articles:
    book = {}
    book['title'] = pod.find('h3').find('a').attrs['title']
    ratestr = pod.find('p').attrs['class'][1]
    starrate = str_to_int(ratestr)
    book['rating'] = starrate
    pricestr = pod.find('div',attrs={'class':'product_price'}).find('p',attrs={'class':'price_color'})
    pricestr = str(pricestr)
    stringlist = pricestr.split('>')
    price = stringlist[1][1:7]
    book['price'] = price
    books.append(book)

print(books)    
    




