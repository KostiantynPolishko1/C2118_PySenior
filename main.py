from bs4 import BeautifulSoup
import requests

print('Lesson 9: Parsing Site')

responce = requests.get('https://coinmarketcap.com/')


if responce.status_code == 200:

    # print('before parser', responce.text)
    item_site = BeautifulSoup(responce.text, features='html.parser')
    coin_rates = item_site.find_all('div', {'class', 'sc-b3fc6b7-0 dzgUIj'})

    for rate in coin_rates:
        # print('rate object -> ', rate)
        price = float(rate.findNext().text[1:].replace(',', ''))
        print('price -> ', price)

