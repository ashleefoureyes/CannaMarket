import re
import sys
import requests

'''
NOTE: This method of obtaining Yahoo Finance data by storing the crumb
value is adapted from Brad Lucas' method found at:

http://blog.bradlucas.com/posts/2017-06-02-new-yahoo-finance-quote-download-url/
'''

#change to most recent time in epoch value
end_date = 1508188071


def split_crumb_store(v):
    return v.split(':')[2].strip('"')


def find_crumb_store(lines):
    # Looking for
    # ,"CrumbStore":{"crumb":"9q.A4D1c.b9
    for l in lines:
        if re.findall(r'CrumbStore', l):
            return l
    print("Did not find CrumbStore")


def get_cookie_value(r):
    return {'B': r.cookies['B']}

def get_page_data(symbol):
    url = "https://finance.yahoo.com/quote/%s/?p=%s" % (symbol, symbol)
    r = requests.get(url)
    cookie = get_cookie_value(r)
    lines = r.content.decode('unicode-escape').strip(). replace('}', '\n')
    return cookie, lines.split('\n')


def get_cookie_crumb(symbol):
    cookie, lines = get_page_data(symbol)
    crumb = split_crumb_store(find_crumb_store(lines))
    return cookie, crumb


def get_data(symbol, start_date, end_date, cookie, crumb):
    filename = 'stock_data/'+'%s.csv' % (symbol)
    url = "https://query1.finance.yahoo.com/v7/finance/download/%s?period1=%s&period2=%s&interval=1d&events=history&crumb=%s" % (symbol, start_date, end_date, crumb)
    response = requests.get(url, cookies=cookie)
    with open (filename, 'wb') as handle:
        for block in response.iter_content(1024):
            handle.write(block)


def download_quotes(symbol):
    cookie, crumb = get_cookie_crumb(symbol)
    start_date = 0
    get_data(symbol, start_date, end_date, cookie, crumb)


if __name__ == '__main__':
    # If we have at least one parameter go ahead and loop overa all the parameters assuming they are symbols
    if len(sys.argv) == 1:
        print("\nUsage: get-yahoo-quotes.py SYMBOL\n\n")
    else:
        for i in range(1, len(sys.argv)):
            symbol = sys.argv[i]
            print("--------------------------------------------------")
            print("Downloading %s to %s.csv" % (symbol, symbol))
            download_quotes(symbol)
            print("--------------------------------------------------")

download_quotes('APH.TO')