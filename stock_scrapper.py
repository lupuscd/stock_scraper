import requests, put_to_xl
from bs4 import BeautifulSoup


final_list = []

def stock_scr():

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

    info_list = [stock_name.text, stock_price.text, stock_pe.text]
    for index, item in enumerate(stock_info):
        info = item.find('span')
        if index > 1:
            info_list.append(info.text)    

    contiue_answer = input('Do you want to add more tickers? y/n: ' )

    if contiue_answer.lower() == 'y':
        final_list.append(info_list)
        info_list.clear()
        stock_scr()
    elif contiue_answer.lower() == 'n':
        final_list.append(info_list)
        put_to_xl.add_to_xl(final_list)
    else:
        print('Wrong input please enter y or n')

stock_scr()
