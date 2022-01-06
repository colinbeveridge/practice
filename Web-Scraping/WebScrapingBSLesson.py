import bs4
import requests


def getHTML(url):
    response = requests.get(url)
    return response.text

html = getHTML('https://www.countrycode.org/')
soup = bs4.BeautifulSoup(html,'html.parser')

table = soup.find('table',attrs = {'class':'main-table'})

countries = []

for row in table.find_all_next('tr'):
    cells = row.find_all_next('td')
    country = {}
    country['name'] = cells[0].string
    countrycodes = cells[2].string
    country['iso-2'] = countrycodes.split('/')[0]
    country['iso-3'] = countrycodes.split('/')[1]
    countries.append(country)

if __name__ == '__main__':
    print(html)
    listcountries = list(countries)
    print(listcountries)
    print(type(table))