from bs4 import BeautifulSoup
import requests

print('Lesson 10: Sqlite3')

responce = requests.get('https://coinmarketcap.com/')
coins_prices = []

if responce.status_code == 200:

    # print('before parser', responce.text)
    item_site = BeautifulSoup(responce.text, features='html.parser')
    coin_rates = item_site.find_all('div', {'class', 'sc-b3fc6b7-0 dzgUIj'})

    for rate in coin_rates:
        # print('rate object -> ', rate)
        temp = rate.findNext().text[1:].replace(',', '')
        price = float(temp)
        # coin_rates.append(temp)
        print('price -> ', price)

print('coins prices', coins_prices)
