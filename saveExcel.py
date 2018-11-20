import requests
from openpyxl import Workbook
import datetime

# This is the code for the Public Api from Coinmarketcap
import requests
from openpyxl import Workbook
import datetime

key = 'a3887cc2-0277-4c38-8335-430d3d01c92c'

api = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY='
api += key

raw_data = requests.get(api).json()
data = raw_data['data']
today = datetime.date.today()

file = Workbook()
sheet = file.create_sheet(str(today),0)

for currency in data:
    sheet.append([currency['name'],
               currency['quote']['USD']['price'],
               currency['quote']['USD']['percent_change_1h'],
               currency['quote']['USD']['percent_change_24h'],
               currency['quote']['USD']['percent_change_7d']])


file.save("Data Analysis.xlsx")