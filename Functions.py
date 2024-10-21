import requests
import pygal
import lxml

apikey = "FVQDMTI5GIVCHLQT"

def TIME_SERIES_INTRADAY(symbol):
    
    interval = input("Please enter the interval: ")

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={"example"}&interval={"example"}min&apikey={apikey}'
    r = requests.get(url)
    data = r.json()

    print(data)