import requests
import bs4


def scrap(page):
    r = requests.get('https://www.olx.pl/praca/warszawa/?page=' + str(page))
    r.raise_for_status()
    print(len(r.text))
    return r.text


f = open('offers.txt', 'w', encoding='utf8')

for i in range(1, 42):
    print("page:" + str(i))
    soup = bs4.BeautifulSoup(scrap(i), 'html.parser')
    offers = soup.find_all('div', {'class': 'offer-wrapper'})
    print(len(offers))
    for j in range(len(offers)):
        offer_string = str(offers[j])
        if 'promoted-list' not in offer_string:
            print(offers[j].select('strong')[0].string)
            f.write(offers[j].select('strong')[0].string)
            f.write('\n')

f.close()
