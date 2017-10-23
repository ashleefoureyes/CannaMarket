from yahoo_finance_bypass import download_quotes

ticker_list = "ticker_list.txt"

def getHistData():
    DAY = '01'
    MONTH = '00' # month must be m - 1
    YEAR = '2013'

    with open(ticker_list) as f:
        stocks = f.readlines()

    for i in range(len(stocks)):
        stock = stocks[i].rstrip('\n')
        download_quotes(stock)


getHistData()

