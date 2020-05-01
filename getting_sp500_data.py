import bs4 as bs
import pickle 
import datetime as dt
import os 
import pandas as pd
import pandas_datareader.data as web
import requests

# pickle serializes any python object 
# os lets us create new directories

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text,'lxml')
    table = soup.find('table', {'id': 'constituents'})
    tickers = []
    
    for row in table.findAll('tr')[1:]:
        ticker = row.find('td').text.strip()
        if "." in ticker:
            ticker = ticker.replace('.','-')
            print('ticker replaced to', ticker) 
        tickers.append(ticker)
        tickers.append(ticker)
    
    with open('sp500tickers.pickle','wb') as f:
        pickle.dump(tickers,f)
        
    return tickers
#save_sp500_tickers()

def get_data_from_yahoo(reload_sp500 = False , reload_prices = False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open('sp500tickers.pickle','rb') as f:
            tickers = pickle.load(f)
            
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2000,1,1)
    end = dt.datetime(2020,4,30)
    c = 0
    print(tickers)
    
    # we can place a condition that checkes if the data needs to be reloaded
    
    for ticker in tickers:
        print(ticker)
        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker,'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker))
            
        else:
            print('Already have {}.csv'.format(ticker))
        
get_data_from_yahoo()
            