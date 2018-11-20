import requests
from prettytable import PrettyTable

key = 'a3887cc2-0277-4c38-8335-430d3d01c92c'

api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api += key

raw_data = requests.get(api).json()
data = raw_data['data']

table = PrettyTable()

for currency in data:
    name = currency['name']
    price = currency['quote']['USD']['price']
    change_1h = currency['quote']['USD']['percent_change_1h']
    change_24h = currency['quote']['USD']['percent_change_24h']
    change_7d = currency['quote']['USD']['percent_change_7d']

    table.add_row([name,price,change_1h,change_24h,change_7d])
table.field_names = ["Name","Price","Change 1h","Change 24h","Change 7d"]
table.sortby = "Change 24h"
table.reversesort = True
print(table)