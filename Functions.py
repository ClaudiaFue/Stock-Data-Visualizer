import requests
import pygal
import lxml

apikey = "FVQDMTI5GIVCHLQT"

def TIME_SERIES_INTRADAY(symbol):
    
    interval = input("Please enter the interval: ")

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}min&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_DAILY(symbol):

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}M&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_DAILY_ADJUSTED(symbol):

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_WEEKLY(symbol):

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_WEEKLY_ADJUSTED(symbol):

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY_ADJUSTED&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_MONTHLY(symbol):

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)

def TIME_SERIES_MONTHLY_ADJUSTED(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol={symbol}&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)
