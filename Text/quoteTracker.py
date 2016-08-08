from googlefinance import getQuotes
import json
import re

def quote_tracker():
    stock_symbols = raw_input("What stock symbol(s) would you like to use? ")
    stock_symbols = re.sub("[^\w]", " ",  stock_symbols).split()
    return json.dumps(getQuotes(stock_symbols), indent=2)

print quote_tracker()
