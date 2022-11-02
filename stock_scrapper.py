import requests, put_to_xl, re
from bs4 import BeautifulSoup


final_list = []
url = 'https://roic.ai/company/'
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

def stock_scr():

    stock_ticker = input('Enter the stock tickers separated by comma: ')
    stock_ticker_list = stock_ticker.split(',')
    
    for ticker in stock_ticker_list:
        
        info_list = []
        final_url = url + ticker.upper()
        page = requests.get(final_url, headers = header)

        soup = BeautifulSoup(page.content, 'html.parser')
        
        stock_name = soup.find('h1', attrs = {'class' : 'uppercase font-semibold text-4xl'})
        stock_price = soup.find('h1', attrs = {'class' : 'uppercase font-semibold self-end text-4xl'})
        stock_pe = soup.find('div', attrs = {'class' : 'inline-block shrink-0'})
        numeric_pe_re = re.findall('\d+\.\d+', stock_pe.text)
        numeric_pe = float(numeric_pe_re[0])
        stock_ey = round((1/numeric_pe) * 100, 1)
        stock_info = soup.find_all('div', attrs = {'class' : 'inline-block shrink-0 ml-9'})

        info_list = [stock_name.text, stock_price.text, numeric_pe, stock_ey]
        for index, item in enumerate(stock_info):
            info = item.find('span')
            if index > 1:
                info_list.append(info.text)  

        final_list.append(info_list)

    contiue_answer = input('Do you want to add more tickers? y/n: ' )

    if contiue_answer.lower() == 'y':
        return stock_scr()
    elif contiue_answer.lower() == 'n':
        return put_to_xl.add_to_xl(final_list)
    else:
        print('Wrong input please enter y or n')

stock_scr()
