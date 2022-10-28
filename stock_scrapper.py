import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
#from openpyxl import load_workbook

url = 'https://roic.ai/company/'
stock_ticker = input('Enter the stock ticker: ')
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
final_url = url + stock_ticker.upper()
page = requests.get(final_url, headers = header)

soup = BeautifulSoup(page.content, 'html.parser')

stock_name = soup.find('h1', attrs = {'class' : 'uppercase font-semibold text-4xl'})
stock_price = soup.find('h1', attrs = {'class' : 'uppercase font-semibold self-end text-4xl'})
stock_pe = soup.find('div', attrs = {'class' : 'inline-block shrink-0'})
stock_info = soup.find_all('div', attrs = {'class' : 'inline-block shrink-0 ml-9'})

info_list = []
for index, item in enumerate(stock_info):
    info = item.find('span')
    if index > 1:
        info_list.append(info.text)    

#Save to excel
wb = Workbook()
sheet = wb.active

